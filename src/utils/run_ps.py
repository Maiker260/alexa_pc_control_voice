import subprocess

def run_ps(command: str):
    ps_command = f'Start-Process powershell -ArgumentList "-Command {command}" -Verb RunAs'

    return subprocess.run(
        ["powershell", "-Command", ps_command],
        check=True
    )