from typing import TYPE_CHECKING

from bot import log

log.setup()

if TYPE_CHECKING:
    from bot.bot import Bot

instance: "Bot" = None  # Global Bot instance.
