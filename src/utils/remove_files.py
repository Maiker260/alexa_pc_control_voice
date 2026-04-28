import os
import logging

def remove_files(directory, files):
    for file in files:
        path = os.path.join(directory, file)

        try:
            if os.path.exists(path):
                os.remove(path)
                logging.info(f"{file} deleted.")
            else:
                logging.info(f"{file} not found, skipping.")
        except Exception:
            logging.exception(f"Error deleting {file}")