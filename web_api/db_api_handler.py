from pymongo import MongoClient
import os

cluster = "mongodb+srv://{}:{}@nianbotdb-ivdrl.gcp.mongodb.net/test?retryWrites=true&w=majority"


class dbApiH:

    def __init__(self):
        self.cluster = MongoClient(cluster.format(os.getenv('db_username'), os.getenv('db_password')))
        self.db = None

    ##--GENERAL--##

    def set_db(self, db_name):
        self.db = self.cluster[db_name]

    def get_document_by_name(self, collection_name):
        if collection_name is None:
            return None
        return self.db[collection_name].find({})

    def get_document_by_id(self, collection_name, id):
        if collection_name is None or id is None:
            return None
        return self.db[collection_name].find_one({"_id": id})

    def delete_all_documents(self, collection_name):
        if collection_name is None:
            return
        self.db[collection_name].delete_many({})

    def delete_document_by_id(self, collection_name, id):
        if collection_name is None:
            return
        self.db[collection_name].delete_one({"_id": id})

    ##--USERS--##

    def add_users(self, users):
        self.db["users"].insert_many([{
            "_id": user.id,
            "name": user.name,
            "joined_at": user.joined_at,
            "messages_sent": 0,
            "commands_used": 0,
            "strikes": 0,
            "nicknames": []
        } for user in users], ordered=False)

    def add_user(self, user):
        self.db["users"].insert_one({
            "_id": user.id,
            "name": user.name,
            "joined_at": user.joined_at,
            "messages_sent": 0,
            "commands_used": 0,
            "strikes": 0,
            "nicknames": []
        })

    def get_alarmed_users(self):
        return self.db["users"].find({"strikes": {"$gt": 0}})

    def get_alarmed_user_by_id(self, id):
        return self.db["users"].find_one({"_id": id, "strikes": {"$gt": 0}})

    def update_user_name_by_id(self, id, new_name):
        self.db["users"].update_one({"_id": id}, {"$set": {"name": new_name}})
        
    def update_user_nicknames_by_id(self, id, old_nick):
        self.db["users"].update_one({"_id": id}, {"$addToSet": {"nicknames": old_nick}})
        
    def get_user_nicknames_by_id(self, id):
        return self.db["users"].find_one({"_id": id})["nicknames"]

    def alarm_user_by_id(self, id):
        self.db["users"].update_one({"_id": id}, {"$inc": {"strikes": 1}})

    def unalarm_user_by_id(self, id):
        self.db["users"].update_one({"_id": id}, {"$inc": {"strikes": -1}})

    def increase_user_messages_by_id(self, id):
        self.db["users"].update_one({"_id": id}, {"$inc": {"messages_sent": 1}})

    def decrease_user_messages_by_id(self, id):
        self.db["users"].update_one({"_id": id}, {"$inc": {"messages_sent": -1}})

    def increase_used_commands_by_id(self, id):
        self.db["users"].update_one({"_id": id}, {"$inc": {"commands_used": 1}})

    def get_top_10_users(self):
        return self.db["users"].find({}).sort([("messages_sent", -1), ("commands_used", -1)]).limit(10)

    def get_all_sent_messages(self):
        return list(self.db["users"].aggregate([{"$group": {"_id": "null", "totalAmount": {"$sum": '$messages_sent'}}}]))

    def get_all_used_commands(self):
        return list(self.db["users"].aggregate([{"$group": {"_id": "null", "totalAmount": {"$sum": 'commands_used'}}}]))

    ##--VIDEOS--##

    def add_videos(self, videos):
        self.db["videos"].insert_many([{
            "_id": video['id'],
            "title": video['title']
        } for video in videos], ordered=False)

    def add_video(self, video):
        self.db["videos"].insert_one({
            "_id": video['id'],
            "title": video['title']
        })

    ##--Q/A--##

    ##--REACTION LISTENERS--##
    
    def add_reactions_listener(self, reactions_listener):
        if self.get_reactions_listener(reactions_listener['name']) is not None:
            return False
        
        self.db["reactions_listeners"].insert_one({
            "name": reactions_listener['name'],
            "message_id": reactions_listener['message_id'],
            "channel_id": reactions_listener['channel_id'],
            "reaction" : reactions_listener['reaction'],
            "text": reactions_listener['text'],
            "status": "running",
            "winner": None
        })
        return True
    
    def set_reactions_listener_reaction(self, name, reaction):
        self.db["reactions_listeners"].update_one({"name": name}, {"$set": {"reaction": reaction}})
        
    def get_reactions_listener(self, name):
        return self.db["reactions_listeners"].find_one({"name": name})
    
    def get_reactions_listeners(self):
        return self.db["reactions_listeners"].find({})
    
    def get_running_reactions_listeners(self):
        return list(filter(lambda x: x["status"] == "running", self.get_reactions_listeners()))
    
    def get_ended_reactions_listeners(self):
        return list(filter(lambda x: x["status"] == "ended", self.get_reactions_listeners()))
    
    def delete_reactions_listener(self, name):
        if self.db["reactions_listeners"].find_one({"name": name})["status"] != "running":
            return
        
        self.db["reactions_listeners"].update_one({"name": name}, {"$set": {"status": "ended"}})

    def end_reactions_listener(self, name, winner_id):
        if self.db["reactions_listeners"].find_one({"name": name})["status"] != "running":
            return
        
        self.db["reactions_listeners"].update_one({"name": name}, [{"$set": {"status": "ended"}}, {"$set": {"winner": winner_id}}])
