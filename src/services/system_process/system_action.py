from .restart_pc import restart_pc
from .shutdown_pc import shutdown_pc

def system_action(data):
    system_action = data.get("system_action", "")

    actions = {
        "restart": restart_pc,
        "shutdown": shutdown_pc,
    }

    if system_action not in actions:
        raise ValueError(f"Invalid system action: {system_action}")

    actions[system_action]()

    return {"message": f"{system_action} executed"}