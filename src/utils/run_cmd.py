import subprocess

def run_cmd(cmd):
    return subprocess.run(
        cmd, 
        check=True,
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )