import subprocess
from src.utils.run_ps import run_ps

def uninstall_cloudflared_package():
    try:
        run_ps('winget uninstall --id Cloudflare.cloudflared -e --silent')
        print("Cloudflared uninstalled via winget.")
    except subprocess.CalledProcessError:
        print("Cloudflared not installed via winget or already removed.")