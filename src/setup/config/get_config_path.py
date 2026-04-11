import os
from src.utils.PATHS import USER_CONFIG_FILES_DIR

def get_app_dir():
    path = USER_CONFIG_FILES_DIR
    os.makedirs(path, exist_ok=True)
    return path


def get_config_path():
    return os.path.join(get_app_dir(), "app_config.json")


def get_yaml_path():
    return os.path.join(get_app_dir(), "config.yml")