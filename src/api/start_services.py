import subprocess
import threading

from src.main import app
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from .wait_for_api import wait_for_api
from .run_api import run_api

def start_services():
    print("Starting Services...")

    threading.Thread(target=lambda: run_api(app), daemon=True).start()

    if not wait_for_api():
        print("API failed to start")
        return

    subprocess.Popen(f'"{CLOUDFLARED_PATH}" tunnel run {tunnel_name}', shell=True)