import subprocess

def restart_pc(data = None):
    subprocess.run(["shutdown", "/r", "f", "/t", "0"])

    return {
        "message": "PC restarting"
    }
