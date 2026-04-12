from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH

def create_tunnel(tunnel_name):
    try:
        run_cmd([CLOUDFLARED_PATH, "tunnel", "create", tunnel_name], True)
    except:
        print("Tunnel probablemente ya existe, continuando...")