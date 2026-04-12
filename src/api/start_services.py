import subprocess
import threading

from src.main import app
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from .wait_for_api import wait_for_api
from .run_api import run_api

def start_services():
    print("Starting Services...")
    threading.Thread(target=run_api, args=(app,), daemon=True).start()

    print("Waiting for API...")
    if not wait_for_api():
        print("API failed to start")
        return

    print("API ready, starting tunnel...")
    # subprocess.Popen(
    #     [CLOUDFLARED_PATH, "tunnel", "run", tunnel_name]
    # )