import os
import time
import shutil
import logging

def remove_directory(path, name):
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            logging.info(f"{name} deleted.")
        except Exception:
            logging.exception(f"Error deleting {name}")
    else:
        logging.info(f"{name} not found, skipping.")