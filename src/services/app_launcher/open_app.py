import subprocess

def open_app(path):
    subprocess.Popen(f'explorer "{path}"', shell=True)