import subprocess
from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH
from src.utils.tunnel_data import tunnel_name

def delete_tunnel():
    try:
        run_cmd([CLOUDFLARED_PATH, "tunnel", "delete", tunnel_name])
        print("Tunnel deletion attempted.")
    except subprocess.CalledProcessError:
        print("Tunnel not found or already deleted.")