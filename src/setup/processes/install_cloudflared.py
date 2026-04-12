import subprocess
from src.utils.run_ps import run_ps

def install_cloudflared():
    print("Installing cloudflared...")
    run_ps("winget install --id Cloudflare.cloudflared --source winget -e --silent")