import discord
from discord.ext import commands
from utils import dataIO

_cd = commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.member)


class eventsHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = dataIO.get_Info("config.json")

        self.ak_emoji_id = 685150420032946236
        self.gn_emoji_id = 893900481649319976
        self.other_games_emoji_id = 691741131360174160
        self.general_emoji_id = 799657215933677578
        self.underage_emoji_name = "🔞"

        self.ak_role_id = 1074345356231454773
        self.gn_role_id = 1074345296093524049
        self.other_games_role_id = 1074345494081458237
        self.general_role_id = 1074345448615202846
        self.underage_role_id = 1074345416650391692

    @commands.Cog.listener()
    async def on_member_join(self, member):
        no_faction = member.guild.get_role(self.config.faction_roles[-1])
        # newcommer = member.guild.get_role(713745424690970686)

        try:
            if self.bot.ww.dbh.get_document_by_id("users", member.id) is None:
                self.bot.ww.dbh.add_user(member)
            # await member.add_roles(no_faction, newcommer)
            await member.add_roles(no_faction)

            """
            embed = discord.Embed(title=f"Welcome to KyoStinV Server {member.name} ",
                                  description="This is a To-Do-List to unlock all chat channel \n"
                                              "- first go to the #rules read them \n"
                                              "- secondly find the confirmation word\n"
                                              "- thirdly go to #confirmation \n"
                                              "- at last paste the word in chat and send it\n"
                                              "with that you unlock all channel \n"
                                              "have a great time here and have fun", color=discord.Color.red())
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed)
        except discord.errors.Forbidden:
            print(f"Failed to send welcome message to {member.name} ")
        """
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        await self.bot.log_channel.send(f'```❗{user} HAS BEEN BANNED```')

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        muted_role = after.guild.get_role(691265959302004797)

        if muted_role in after.roles and muted_role not in before.roles:
            await self.bot.log_channel.send(f'```❗{after} HAS BEEN MUTED```')
        elif muted_role in before.roles and muted_role not in after.roles:
            await self.bot.log_channel.send(f'```❗{after} HAS BEEN UNMUTED```')

        if before.nick != after.nick:
            self.bot.ww.dbh.update_user_nicknames_by_id(after.id, before.nick)

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            self.bot.ww.dbh.update_user_name_by_id(after.id, after.name)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id != 1073995608572039209:
            return

        member = payload.member
        guild = member.guild

        role_to_add = None

        if payload.message_id == 1074025916742770768:
            if payload.emoji.id == self.ak_emoji_id:
                role_to_add = guild.get_role(self.ak_role_id)
            elif payload.emoji.id == self.gn_emoji_id:
                role_to_add = guild.get_role(self.gn_role_id)
            elif payload.emoji.id == self.other_games_emoji_id:
                role_to_add = guild.get_role(self.other_games_role_id)
            elif payload.emoji.id == self.general_emoji_id:
                role_to_add = guild.get_role(self.general_role_id)
            elif payload.emoji.name == self.underage_emoji_name:  # we need to check the name here (?)
                role_to_add = guild.get_role(self.underage_role_id)

        if payload.message_id == 884754266902921218: #??
            role_to_add = guild.get_role(877197372239802389)

        if role_to_add is not None:
            await member.add_roles(role_to_add)
            print(f'{member.name} joined {role_to_add.name}')
        else:
            print(f'{member.name} attempted to join an invalid role')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id != 1073995608572039209:
            return

        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        role_to_remove = None

        if payload.message_id == 1074025916742770768:
            if payload.emoji.id == self.ak_emoji_id:
                role_to_remove = guild.get_role(self.ak_role_id)
            elif payload.emoji.id == self.gn_emoji_id:
                role_to_remove = guild.get_role(self.gn_role_id)
            elif payload.emoji.id == self.other_games_emoji_id:
                role_to_remove = guild.get_role(self.other_games_role_id)
            elif payload.emoji.id == self.general_emoji_id:
                role_to_remove = guild.get_role(self.general_role_id)
            elif payload.emoji.name == self.underage_emoji_name:  # we need to check the name here (?)
                role_to_remove = guild.get_role(self.underage_role_id)

        if payload.message_id == 884754266902921218: #??
            role_to_remove = guild.get_role(877197372239802389)

        if role_to_remove is not None:
            await member.remove_roles(role_to_remove)
            print(f'{member.name} joined {role_to_remove.name}')
        else:
            print(f'{member.name} attempted to leave an invalid role')


def setup(bot):
    bot.add_cog(eventsHandler(bot))
