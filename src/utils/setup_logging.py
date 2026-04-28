import logging
import os
from src.utils.PATHS import USER_CONFIG_FILES_DIR

def setup_logging():
    log_path = os.path.join(USER_CONFIG_FILES_DIR, "log.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )