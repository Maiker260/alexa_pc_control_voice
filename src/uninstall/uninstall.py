import subprocess
import os
import shutil
import ctypes
import sys
from src.utils.run_ps import run_ps
from src.utils.run_cmd import run_cmd
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH, CLOUDFLARED_DIR, USER_CONFIG_FILES_DIR

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uninstall_cloudflared():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

    # Stop process
    try:
        run_cmd(["taskkill", "/F", "/IM", "cloudflared.exe"])
        print("Cloudflared process stopped.")
    except subprocess.CalledProcessError:
        print("Cloudflared process was not running.")

    # Delete tunnel
    try:
        run_cmd([CLOUDFLARED_PATH, "tunnel", "delete", tunnel_name])
        print("Tunnel deletion attempted.")
    except subprocess.CalledProcessError:
        print("Tunnel not found or already deleted. Skipping.")

    # Remove certs / login data
    run_ps(
        'if (Test-Path $env:USERPROFILE\\.cloudflared) { Remove-Item -Recurse -Force $env:USERPROFILE\\.cloudflared }'
    )

    # Delete folders safely
    if os.path.exists(CLOUDFLARED_DIR):
        shutil.rmtree(CLOUDFLARED_DIR)
        print("CLOUDFLARED_DIR deleted.")
    else:
        print("CLOUDFLARED_DIR not found, skipping.")

    if os.path.exists(USER_CONFIG_FILES_DIR):
        shutil.rmtree(USER_CONFIG_FILES_DIR)
        print("USER_CONFIG_FILES_DIR deleted.")
    else:
        print("USER_CONFIG_FILES_DIR not found, skipping.")

    # Uninstall via winget
    try:
        run_ps('winget uninstall --id Cloudflare.cloudflared -e --silent')
    except subprocess.CalledProcessError:
        print("Cloudflared not installed via winget or already removed.")

    print("Cloudflared removed successfully")