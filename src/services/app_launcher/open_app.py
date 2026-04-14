import subprocess
import shutil

def open_app(name, path=None):
    cmd = shutil.which(name)
    if cmd:
        subprocess.Popen([cmd])
        return

    if path:
        subprocess.Popen(f'explorer "{path}"', shell=True)
        return

    raise RuntimeError("App cannot be opened")