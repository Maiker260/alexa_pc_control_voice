import time
import subprocess
import logging

from src.utils.PATHS import CLOUDFLARED_PATH

def wait_for_tunnel_close(tunnel_name, timeout=90, check_only=False):
    start = time.time()

    while True:
        result = subprocess.run(
            [CLOUDFLARED_PATH, "tunnel", "info", tunnel_name],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        if result.returncode != 0:
            logging.warning("Error checking tunnel status")
            return False

        if "does not have any active connection" in result.stdout:
            logging.info("Tunnel fully disconnected.")
            return True

        if check_only:
            return False

        if time.time() - start > timeout:
            logging.warning("Timeout waiting for tunnel closure.")
            return False

        logging.info("Waiting for tunnel to close...")
        time.sleep(5)