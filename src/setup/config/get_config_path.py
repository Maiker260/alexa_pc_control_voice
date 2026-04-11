import os

def get_config_path():
    base_dir = os.getenv("APPDATA")
    app_dir = os.path.join(base_dir, "Alexa PC Control Voice")
    os.makedirs(app_dir, exist_ok=True)
    
    return os.path.join(app_dir, "app_config.json")