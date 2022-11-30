import asyncio

import discord
from discord.ext import commands

import bot
from bot import constants
from bot.bot import Bot, StartupError


async def main() -> None:
    """Entry async method for starting the bot."""
    intents = discord.Intents.all()
    intents.presences = False

    bot.instance = Bot(
        guild_id=constants.Guild.id,
        command_prefix=commands.when_mentioned_or(constants.Bot.prefix),
        activity=discord.Game(name=f"List Commands: {constants.Bot.prefix}help"),
        case_insensitive=True,
        intents=intents,
    )
    async with bot.instance as _bot:
        await _bot.start(constants.Bot.token)

try:
    asyncio.run(main())
except StartupError as e:
    message = "Unknown Startup Error Occurred."

    print(e.exception)

    exit(1)
