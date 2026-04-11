import subprocess

def run_ps(command):
    subprocess.run(["powershell", "-Command", command], check=True)