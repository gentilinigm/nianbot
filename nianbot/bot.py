import asyncio
import logging
import types
from contextlib import suppress

import aiohttp
import discord
from discord.ext import commands
from psycopg2.extensions import connection

from nianbot import exts
from nianbot.utils.extensions import walk_extensions
from nianbot.utils.scheduling import create_task


class StartupError(Exception):
    """Exception class for startup errors."""

    def __init__(self, base: Exception):
        super().__init__()
        self.exception = base


class Bot(commands.Bot):
    """A nianbot subclass that implements some features."""

    def __init__(
            self,
            *args,
            guild_id: int,
            http_session: aiohttp.ClientSession,
            db_connection: connection,
            **kwargs
    ):
        """
        Initialise the base nianbot instance.

        Args:
            guild_id: The ID of the KyoStinV guild.
            http_session: The aiohttp.ClientSession()
            db_connection: The active Postgresql connection
        """
        super().__init__(
            *args,
            **kwargs
        )

        self.guild_id = guild_id
        self.http_session = http_session
        self.db_connection = db_connection

        self._guild_available: asyncio.Event | None = None
        self._extension_loading_task: asyncio.Task | None = None

    async def setup_hook(self) -> None:
        """Default async initialisation method for discord.py."""
        await super().setup_hook()

        self._guild_available = asyncio.Event()

        await self.load_extensions(exts)

    async def _load_extensions(self, module: types.ModuleType) -> None:
        """Load all the extensions within the given module and save them to ``self.all_extensions``."""
        logging.info("Waiting for guild %d to be available before loading extensions.", self.guild_id)

        await self.wait_until_guild_available()
        logging.info("Loading extensions...")
        self.all_extensions = walk_extensions(module)

        for extension in self.all_extensions:
            create_task(self.load_extension(extension))

    async def _sync_app_commands(self) -> None:
        """Sync global & guild specific application commands after extensions are loaded."""
        await self._extension_loading_task
        await self.tree.sync()
        await self.tree.sync(guild=discord.Object(self.guild_id))

    async def load_extensions(self, module: types.ModuleType, sync_app_commands: bool = True) -> None:
        """Load all the extensions within the given ``module`` and save them to ``self.all_extensions``."""
        self._extension_loading_task = create_task(self._load_extensions(module))
        if sync_app_commands:
            create_task(self._sync_app_commands())

    async def on_guild_available(self, guild: discord.Guild) -> None:
        """
        Set the internal guild available event when self.guild_id becomes available.

        If the cache appears to still be empty (no members, no channels, or no roles), the event
        will not be set and `guild_available_but_cache_empty` event will be emitted.
        """
        if guild.id != self.guild_id:
            return

        if not guild.roles or not guild.members or not guild.channels:
            logging.error("Guild available event was dispatched but the cache appears to still be empty!")
            return

        self._guild_available.set()

    async def on_guild_unavailable(self, guild: discord.Guild) -> None:
        """Clear the internal guild available event when self.guild_id becomes unavailable."""
        if guild.id != self.guild_id:
            return

        self._guild_available.clear()

    async def wait_until_guild_available(self) -> None:
        """
        Wait until the guild that matches the ``guild_id`` given at init is available (and the cache is ready).

        The on_ready event is inadequate because it only waits 2 seconds for a GUILD_CREATE
        gateway event before giving up and thus not populating the cache for unavailable guilds.
        """
        await self._guild_available.wait()

    async def close(self) -> None:
        """Closes connections (Discord, aiohttp session, etc)."""
        for ext in list(self.extensions):
            with suppress(Exception):
                await self.unload_extension(ext)

        for cog in list(self.cogs):
            with suppress(Exception):
                await self.remove_cog(cog)

        await super().close()

        if self.db_connection:
            await self.db_connection.close()

        if self.http_session:
            await self.http_session.close()
