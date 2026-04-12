from src.utils.load_user_config import load_user_config

def get_api_key():
    config = load_user_config()
    return config["api_key"]