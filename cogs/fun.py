import random
import discord
from discord.ext import commands
from utils import permissions, dataIO, utils

# todo better hotcalc cheat system (xd)
# todo fun commands: {add here}

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = dataIO.get_Info("config.json")

    @commands.command(
        name="coinflip",
        help="What will you get? *heads* or *tails*?",
        description="The coinflip command!",
        aliases=["flip", "coin", "cf"]
    )
    @permissions.is_in_channel(684786580937900043)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _coinflip(self, ctx):
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.mention}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command(
        name="randomwaifu",
        help="Returns a random waifu *emoji*",
        description="The randomwaifu command!",
        hidden=True,
        aliases=["rw"],
    )
    @permissions.is_in_channel(684786580937900043)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _randomwaifu(self, ctx):
        await ctx.send("*Command removed*")
        """
        waifu_emotes = [ctx.bot.get_emoji(emoji.id) for emoji in self.bot.emojis if 'waifu' in emoji.name.lower()]
        try:
            await ctx.send(f"**{ctx.author.mention}** you got {random.choice(waifu_emotes)}")
        except:
            await ctx.send(f"Are there any waifu emojis?")
        """

    @commands.command(
        name="hotcalc",
        help="Returns a random percent for how hot a member is",
        description="The hotcalc command!",
        aliases=["howhot", "hot"]
    )
    @permissions.is_in_channel(684786580937900043)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _hotcalc(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        random.seed(user.id)
        r = random.randint(1, 100)
        hot = 100000000 if user.id == self.bot.user.id else r / 1.17

        if user.id == 464426467032301568:
            hot = -1

        if user.id == 310852581385699340:
            hot = 95.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.nick if user.nick is not None else user.name}** is **{hot:.2f}%** hot {emoji}")

    @commands.command(
        name="reverse",
        help="Everything you type after reverse will be reversed",
        description="!dnammoc esrever ehT",
        aliases=[]
    )
    @permissions.is_in_channel(684786580937900043)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command(
        name="msgleaderboard",
        help="shows the top 10 members, based on massages and commands used",
        description="The msgleaderboard command!",
        aliases=["msgtop10", "msgl"]
    )
    @permissions.is_in_channel(684786580937900043)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _msgleaderboard(self, ctx):
        members = list(self.bot.ww.dbh.get_top_10_users())
        for member in members:
            if member["_id"] == 310852581385699340:
                members.remove(member)
        members.insert(0, {"_id": 310852581385699340, "messages_sent": "∞", "commands_used": "∞"})
        loop = [f"**{(ctx.guild.get_member(member['_id']).nick or ctx.guild.get_member(member['_id']).name) if ctx.guild.get_member(member['_id']) is not None else member['name']}** - **__{member['messages_sent']}__** total sent messages | **__{member['commands_used']}__** total used commands" for member in members[:10]]
        await utils.prettyResults(
            ctx, "name", f"**Top 10 members**", loop
        )


async def setup(client):
    await client.add_cog(Fun(client))
