import subprocess

def run_ps(command: str, admin = None):
    ps_command = f'Start-Process powershell -ArgumentList "-Command {command}" -Verb RunAs' if admin else command

    return subprocess.run(
        ["powershell", "-Command", ps_command],
        check=True
    )