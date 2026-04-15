import subprocess
import shutil

def open_app(name, path=None):
    # Apps included in the system PATH
    cmd = shutil.which(name) or shutil.which(name + ".exe")
    if cmd:
        subprocess.Popen([cmd])
        return

    # Windows Store apps
    try:
        subprocess.Popen(f"start {name}:", shell=True)
        return
    except:
        pass

    # Third-party app installed
    if path:
        subprocess.Popen(f'explorer "{path}"', shell=True)
        return

    raise RuntimeError("App cannot be opened")