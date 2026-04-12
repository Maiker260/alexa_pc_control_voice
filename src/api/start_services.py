import subprocess
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from .wait_for_api import wait_for_api
from .run_api import run_api

def start_services():
    print("Starting Services...")
    subprocess.Popen(
        ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("Waiting for API...")
    if not wait_for_api():
        print("API failed to start")
        return

    print("API ready, starting tunnel...")
    subprocess.Popen(
        [CLOUDFLARED_PATH, "tunnel", "run", tunnel_name]
    )