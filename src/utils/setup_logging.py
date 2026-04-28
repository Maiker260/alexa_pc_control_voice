import logging
from logging.handlers import RotatingFileHandler
import os

from src.utils.PATHS import USER_CONFIG_FILES_DIR

def setup_logging():
    log_path = os.path.join(USER_CONFIG_FILES_DIR, "launcher.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    handler = RotatingFileHandler(
        log_path,
        maxBytes=1_000_000, #1 MB
        backupCount=5 # 5 log files
    )

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(handler)


def setup_uvicorn_logging():

    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers = []
        logger.propagate = True