from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot.bot import Bot

instance: "Bot" = None  # Global Bot instance.
