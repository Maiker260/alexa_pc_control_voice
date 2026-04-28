import subprocess
import os
import threading
import subprocess
import logging
from src.main import app
from src.utils.tunnel_data import tunnel_name
from src.utils.PATHS import CLOUDFLARED_PATH
from src.api.run_api import run_api
from src.utils.get_config_path import get_config_path, get_yaml_path
from src.api.wait_for_port import wait_for_port
from src.utils.setup_logging import setup_logging, setup_uvicorn_logging
from .process_manager import process as pm

def safe_run_api():
    try:
        run_api(app)
    except Exception:
        logging.exception("FastAPI crashed")

def start_services():
    # Start Logging
    setup_logging()
    setup_uvicorn_logging()

    CREATE_NO_WINDOW = 0x08000000

    # Check if the config exists
    if not os.path.exists(get_config_path()):
        print("ERROR: Application not installed. Run the installer first.")
        return
    
    config_path = get_yaml_path()

    # Start FastAPI
    logging.info("Starting FastAPI...")

    threading.Thread(
        target=safe_run_api,
        daemon=True
    ).start()

    if wait_for_port("127.0.0.1", 8000):
        logging.info("FastAPI is running.")
    else:
        logging.error("FastAPI failed to start")
        return

    # Start Cloudflared
    logging.info("Starting tunnel...")
    try:
        pm.process = subprocess.Popen([
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
        
        logging.info("Tunnel running.")
    except Exception:
        logging.exception("Error starting tunnel")