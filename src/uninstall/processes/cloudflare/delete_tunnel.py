import subprocess
import logging
from src.utils.PATHS import CLOUDFLARED_PATH
from src.utils.tunnel_data import tunnel_name

def delete_tunnel():
    try:
        subprocess.run([
            CLOUDFLARED_PATH,
            "tunnel",
            "delete",
            tunnel_name
        ], check=True)
        
        logging.info("Tunnel deleted successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to delete tunnel: {e}")