from typing import TYPE_CHECKING

from nianbot import log

log.setup()

if TYPE_CHECKING:
    from nianbot.bot import Bot

instance: "Bot" = None  # Global Bot instance.
