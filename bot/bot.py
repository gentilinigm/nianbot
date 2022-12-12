from contextlib import suppress

import aiohttp
import psycopg2
from discord.ext import commands


class StartupError(Exception):
    """Exception class for startup errors."""

    def __init__(self, base: Exception):
        super().__init__()
        self.exception = base


class Bot(commands.Bot):
    """A subclass that implements some features."""

    def __init__(
            self,
            *args,
            guild_id: int,
            http_session: aiohttp.ClientSession,
            db_connection: psycopg2,
            **kwargs
    ):
        """
        Initialise the base bot instance.

        Args:
            guild_id: The ID of the KyoStinV guild.
        """
        super().__init__(
            *args,
            **kwargs
        )

        self.http_session = http_session
        self.db_connection = db_connection
        self.guild_id = guild_id

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
