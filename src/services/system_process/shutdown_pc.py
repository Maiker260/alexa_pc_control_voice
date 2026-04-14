import subprocess

def shutdown_pc(data = None):
    subprocess.run(["shutdown", "/s", "f", "/t", "0"])

    return {
        "message": "PC Shutting down"
    }