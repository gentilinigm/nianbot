import asyncio
import logging

import aiohttp
import discord
import psycopg2
from discord.ext import commands
from psycopg2 import DatabaseError
from psycopg2.extensions import connection

import nianbot
from nianbot import constants
from nianbot.bot import Bot, StartupError


async def _create_db_connection() -> connection:
    try:
        conn = psycopg2.connect(
            dbname=constants.Database.dbname,
            user=constants.Database.user,
            password=constants.Database.password,
            host=constants.Database.host,
            port=constants.Database.port
        )
    except DatabaseError as e:
        raise StartupError(e)

    return conn


async def main() -> None:
    """Entry async method for starting the nianbot."""
    intents = discord.Intents.all()
    intents.presences = False

    async with aiohttp.ClientSession() as session:
        nianbot.instance = Bot(
            guild_id=constants.Guild.id,
            http_session=session,
            db_connection=await _create_db_connection(),
            command_prefix=commands.when_mentioned_or(constants.Bot.prefix),
            activity=discord.Game(name=f"List Commands: {constants.Bot.prefix}help"),
            case_insensitive=True,
            intents=intents,
        )
    async with nianbot.instance as _bot:
        await _bot.start(constants.Bot.token)


try:
    asyncio.run(main())
except StartupError as e:
    message = "Unknown Startup Error Occurred."

    if isinstance(e.exception, DatabaseError):
        message = "Could not connect to postgresql"

    logging.fatal(e.exception)
    logging.fatal(message)

    exit(1)
