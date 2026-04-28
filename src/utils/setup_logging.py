import logging
from logging.handlers import RotatingFileHandler
import os

from src.utils.PATHS import USER_CONFIG_FILES_DIR

def setup_logging(log_name, level=logging.INFO, max_bytes=1_000_000, backup_count=5):
    log_path = os.path.join(USER_CONFIG_FILES_DIR, log_name)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    handler = RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backup_count
    )

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(handler)


def setup_uvicorn_logging():

    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers = []
        logger.propagate = True