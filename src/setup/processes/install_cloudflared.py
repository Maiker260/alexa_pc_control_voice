import subprocess

def install_cloudflared():
    print("Installing cloudflared...")
    subprocess.run("winget install --id Cloudflare.cloudflared --source winget -e --silent", shell=True)