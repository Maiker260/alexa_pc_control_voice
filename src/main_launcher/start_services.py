import subprocess
import os
import threading
import subprocess
from src.main import app
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from src.api.run_api import run_api
from src.utils.get_config_path import get_config_path, get_yaml_path
from src.api.wait_for_port import wait_for_port

process = None

def start_services():
    CREATE_NO_WINDOW = 0x08000000

    global process

    # Check if the config exists
    if not os.path.exists(get_config_path()):
        print("ERROR: Application not installed. Run the installer first.")
        return
    
    config_path = get_yaml_path()

    # Start FastAPI
    print("Starting FastAPI...")

    threading.Thread(
        target=run_api,
        args=(app,),
        daemon=True
    ).start()

    wait_for_port("127.0.0.1", 8000)

    print("FastAPI is running.")

    # Start Cloudflared
    print("Starting tunnel...")
    try:
        process = subprocess.Popen([
            CLOUDFLARED_PATH,
            "tunnel",
            "--config",
            config_path,
            "run",
            tunnel_name
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=CREATE_NO_WINDOW
        )
        
        print("Tunnel running.")
    except Exception as e:
        print(f"Error starting tunnel: {e}")

    print("Starting Services...")
    threading.Thread(target=run_api, args=(app,), daemon=True).start()