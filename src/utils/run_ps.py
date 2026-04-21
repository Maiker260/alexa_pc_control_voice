import subprocess

def run_ps(command: str):
    return subprocess.run(
        ["powershell", "-Command", command],
        check=True
    )