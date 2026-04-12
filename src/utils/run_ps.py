import subprocess

def run_ps(command: str, no_window: bool = False):

    return subprocess.run(
        ["powershell", "-Command", 
        command], 
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW if no_window else 0
    )