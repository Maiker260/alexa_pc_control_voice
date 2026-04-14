from src.services.app_launcher.launch_app import launch_app
from src.services.system_process.restart_pc import restart_pc
from src.services.system_process.shutdown_pc import shutdown_pc

def handle_request(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid request format")

    action = data.get("action")

    if not action:
        raise ValueError("Missing action")

    actions = {
        "open_application": launch_app,
        "restart_pc": restart_pc,
        "shutdown_pc": shutdown_pc,
    }

    if action not in actions:
        raise ValueError(f"Invalid action: {action}")

    return actions[action](data)