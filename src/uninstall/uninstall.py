import subprocess
import os
import shutil
import ctypes
import sys
from src.utils.tunnel_data import tunnel_name

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

CLOUDFLARED_PATH = r"C:\Program Files (x86)\cloudflared\cloudflared.exe"
CLOUDFLARED_DIR = r"C:\Program Files (x86)\cloudflared"
USER_DATA_DIR = os.path.join(os.environ["USERPROFILE"], ".cloudflared")

def run_ps(command):
    subprocess.run(["powershell", "-Command", command], check=True)

def uninstall_cloudflared():
    # 1. Delete tunnel
    run_ps(f"cloudflared.exe tunnel delete {tunnel_name}")

    # 2. Remove certs / login data
    run_ps(f"Remove-Item -Recurse -Force $env:USERPROFILE\\.cloudflared")

    # 3. Stop process
    try:
        run_ps("taskkill /F /IM cloudflared.exe")
        print("Cloudflared process stopped.")
    except subprocess.CalledProcessError:
        print("Cloudflared process was not running.")

    # 4. Delete executable and folder
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