import shutil

def is_cloudflared_installed():
    return shutil.which("cloudflared") is not None