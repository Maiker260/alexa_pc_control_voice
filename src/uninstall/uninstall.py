import subprocess
import os
import shutil
import ctypes
import sys
from .run_ps import run_ps
# from utils.tunnel_data import tunnel_name
from utils.PATHS import CLOUDFLARED_PATH, CLOUDFLARED_DIR, USER_DATA_DIR

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

def uninstall_cloudflared():
    tunnel_name = "alexa-tunnel"

    # Stop process
    try:
        run_ps("taskkill /F /IM cloudflared.exe")
        print("Cloudflared process stopped.")
    except subprocess.CalledProcessError:
        print("Cloudflared process was not running.")

    # Delete tunnel
    try:
        run_ps(f'"{CLOUDFLARED_PATH}" tunnel delete {tunnel_name}', check=False)
        print("Tunnel deletion attempted.")
    except Exception as e:
        print(f"Tunnel deletion failed: {e}")

    # Remove certs / login data
    run_ps('if (Test-Path $env:USERPROFILE\\.cloudflared) { Remove-Item -Recurse -Force $env:USERPROFILE\\.cloudflared }')

    # Delete executable and folder
    if os.path.exists(CLOUDFLARED_DIR):
        try:
            shutil.rmtree(CLOUDFLARED_DIR)
            print(f"Cloudflared folder '{CLOUDFLARED_DIR}' deleted.")
        except PermissionError:
            print(f"Permission denied. Run the script as administrator to delete '{CLOUDFLARED_DIR}'.")
        except Exception as e:
            print(f"Failed to delete folder: {e}")
    else:
        print("Cloudflared folder not found, skipping deletion.")

    print("Cloudflared removed successfully")