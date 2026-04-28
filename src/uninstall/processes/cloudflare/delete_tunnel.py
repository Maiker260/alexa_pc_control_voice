import subprocess
import logging
import time
from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH
from src.utils.tunnel_data import tunnel_name

def delete_tunnel():
    for attempt in range(3):
        try:
            result = run_cmd([
                CLOUDFLARED_PATH,
                "tunnel",
                "delete",
                tunnel_name
            ])

            logging.info(f"Tunnel deleted: {result}")
            return

        except subprocess.CalledProcessError as e:
            logging.error(f"Delete attempt {attempt+1} failed: {e}")
            time.sleep(2)

    logging.error("Failed to delete tunnel after retries")