from src.services.app_launcher.launch_app import launch_app
from src.services.system_process.system_action import system_action
from src.services.music_player.play_music import play_music

def handle_request(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid request format")

    action = data.get("action")

    if not action:
        raise ValueError("Missing action")

    actions = {
        "music": play_music,
        "open_application": launch_app,
        "system": system_action,
    }

    if action not in actions:
        raise ValueError(f"Invalid action: {action}")

    return actions[action](data)