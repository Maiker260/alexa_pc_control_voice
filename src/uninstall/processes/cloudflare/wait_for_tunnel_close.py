import time
import subprocess
import logging

from src.utils.PATHS import CLOUDFLARED_PATH

def wait_for_tunnel_close(tunnel_id, timeout=90):
    start = time.time()

    while time.time() - start < timeout:
        result = subprocess.run(
            [CLOUDFLARED_PATH, "tunnel", "info", tunnel_id],
            capture_output=True,
            text=True
        )

        if "Connections: 0" in result.stdout:
            logging.info("Tunnel fully disconnected.")
            return True
        
        logging.info("Waiting for tunnel to close...")
        time.sleep(5)
        
    logging.warning("Timeout waiting for tunnel closure.")

    return False