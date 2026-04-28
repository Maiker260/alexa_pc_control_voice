import subprocess
import logging
from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH

def stop_cloudflared():
    try:
        run_cmd(["taskkill", "/F", "/IM", CLOUDFLARED_PATH])
        logging.info("Cloudflared process stopped.")
    except subprocess.CalledProcessError:
        logging.info("Cloudflared process was not running.")