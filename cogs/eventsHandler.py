import discord
from discord.ext import commands
from utils import dataIO

_cd = commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.member)

ak_emoji_id = 685150420032946236
gn_emoji_id = 893900481649319976
other_games_emoji_id = 691741131360174160
general_emoji_id = 799657215933677578
underage_emoji_name = "🔞"

ak_role_id = 1074345356231454773
gn_role_id = 1074345296093524049
other_games_role_id = 1074345494081458237
general_role_id = 1074345448615202846
underage_role_id = 1074345416650391692


class eventsHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = dataIO.get_Info("config.json")

        guild = self.bot.get_guild(684039093927280664)

        ak_role = guild.get_role(ak_role_id)
        gn_role = guild.get_role(gn_role_id)
        other_games_role = guild.get_role(other_games_role_id)
        general_role = guild.get_role(general_role_id)
        underage_role = guild.get_role(underage_role_id)

        self.roles_map = {
            ak_emoji_id: ak_role,
            gn_emoji_id: gn_role,
            other_games_emoji_id: other_games_role,
            general_emoji_id: general_role,
            underage_emoji_name: underage_role
        }

        print(self.roles_map)

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
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id != 1073995608572039209 or reaction.message.id != 1074377698681573446:
            return

        emoji_id = reaction.emoji.id

        print(emoji_id)

        if emoji_id in self.roles_map:
            user.add_roles(self.roles_map[emoji_id])
            print(f'{user.name} joined {self.roles_map[emoji_id].name}')
        else:
            print(f'{user.name} could not join the role {emoji_id}, something went wrong')

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.channel.id != 1073995608572039209 or reaction.message.id != 1074377698681573446:
            return

        emoji_id = reaction.emoji.id

        if emoji_id in self.roles_map:
            user.remove_roles(self.roles_map[emoji_id])
            print(f'{user.name} left {self.roles_map[emoji_id].name}')
        else:
            print(f'{user.name} could not leave the role {emoji_id}, something went wrong')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass  # will use in the future

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        pass  # will use in the future


def setup(bot):
    bot.add_cog(eventsHandler(bot))
