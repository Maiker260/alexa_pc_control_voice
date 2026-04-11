import subprocess

def install_cloudflared():
    print("Installing cloudflared...")
    subprocess.run("winget install Cloudflare.cloudflared -e --silent", shell=True)