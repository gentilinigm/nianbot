import logging
import os
import sys
from logging import handlers
from pathlib import Path

import coloredlogs

from bot import constants

TRACE_LEVEL = 5


def setup() -> None:
    """Set up loggers."""
    root_log = logging.getLogger()

    format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(format_string)

    if constants.FILE_LOGS:
        log_file = Path("logs", "bot.log")
        log_file.parent.mkdir(exist_ok=True)
        file_handler = handlers.RotatingFileHandler(log_file, maxBytes=5242880, backupCount=7, encoding="utf8")
        file_handler.setFormatter(formatter)
        root_log.addHandler(file_handler)

        if "COLOREDLOGS_LEVEL_STYLES" not in os.environ:
            coloredlogs.DEFAULT_LEVEL_STYLES = {
                **coloredlogs.DEFAULT_LEVEL_STYLES,
                "trace": {"color": 246},
                "critical": {"background": "red"},
                "debug": coloredlogs.DEFAULT_LEVEL_STYLES["info"]
            }

        if "COLOREDLOGS_LOG_FORMAT" not in os.environ:
            coloredlogs.DEFAULT_LOG_FORMAT = format_string

        coloredlogs.install(level=TRACE_LEVEL, logger=root_log, stream=sys.stdout)
