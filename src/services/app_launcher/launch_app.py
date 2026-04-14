from .find_app import find_app
from .open_app import open_app

def launch_app(data):
    app_exception = {
        "lolito": "league of legends",
    }

    app_name = data.get("app_name", "")
    
    if not app_name:
        raise ValueError("app_name is required")

    name = app_exception.get(app_name, app_name)

    path = find_app(name)

    if path:
        open_app(path)

        return {
            "message": "App opened",
            "app": name
        }
        
    else:
        raise RuntimeError("App not found")