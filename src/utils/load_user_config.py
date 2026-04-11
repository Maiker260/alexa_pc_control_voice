import json
from src.setup.config.get_config_path import get_config_path

def load_user_config():
    try:
        path = get_config_path()

        with open(path, "r") as f:
            config = json.load(f)

    except FileNotFoundError:
        raise RuntimeError("app_config.json not found")
    
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON in app_config.json")

    if "api_key" not in config or not config["api_key"]:
        raise RuntimeError("Missing or empty 'api_key' in config")

    return config