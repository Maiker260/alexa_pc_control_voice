import json

def load_config():
    try:
        with open("app_config.json") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise RuntimeError("app_config.json not found")
    except json.JSONDecodeError:
        raise RuntimeError("Invalid JSON in app_config.json")

    if "api_key" not in config or not config["api_key"]:
        raise RuntimeError("Missing or empty 'api_key' in config")

    return config