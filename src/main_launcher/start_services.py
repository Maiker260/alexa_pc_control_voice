import subprocess
import os
import sys
import signal

from src.main import app
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from src.api.run_api import run_api
from src.utils.get_config_path import get_config_path, get_yaml_path

process = None

def start_services():
    global process

    # Check if the config exists
    if not os.path.exists(get_config_path()):
        print("ERROR: Application not installed. Run the installer first.")
        return
    
    config_path = get_yaml_path()

    # Run the API
    print("Starting tunnel...")
    try:
        subprocess.Popen([
            CLOUDFLARED_PATH,
            "tunnel",
            "--config",
            config_path,
            "run",
            tunnel_name
        ], 
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
        
        print("Tunnel running.")
    except Exception as e:
        print(f"Error starting tunnel: {e}")

    # Terminate the process correctly
    def shutdown(sig, frame):
        print("Shutting down...")
        if process:
            process.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)

    print("Starting Services...")
    run_api(app)