import json
from src.utils.get_config_path import get_config_path

def save_app_config(domain, api_key, tunnel_name):
    config = {
        "domain": domain,
        "api_key": api_key,
        "tunnel_name": tunnel_name
    }

    path = get_config_path()

    with open(path, "w") as f:
        json.dump(config, f, indent=4)

    return path