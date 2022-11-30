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

        self.guild_id = guild_id
