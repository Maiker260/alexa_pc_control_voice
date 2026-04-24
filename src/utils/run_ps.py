import subprocess

def run_ps(command: str):
    return subprocess.run(
        ["powershell", "-Command", command],
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )