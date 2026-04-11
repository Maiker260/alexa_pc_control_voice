import json

def save_app_config(domain, api_key):
    config = {
        "domain": domain,
        "api_key": api_key
    }

    with open("app_config.json", "w") as f:
        json.dump(config, f, indent=4)