from .load_user_config import load_user_config

def get_keys():
    config = load_user_config()
    return config["api_key"], config["device_secret"]