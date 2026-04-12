import os
from src.utils.PATHS import USER_DATA_DIR

def get_credentials_file():
    path = USER_DATA_DIR

    for file in os.listdir(path):
        if file.endswith(".json"):
            return os.path.join(path, file)

    raise Exception("No credentials file (.json)")
