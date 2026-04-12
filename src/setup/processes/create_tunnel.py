from .run import run
from src.utils.PATHS import CLOUDFLARED_PATH

def create_tunnel(tunnel_name):
    run([CLOUDFLARED_PATH, "tunnel", "create", {tunnel_name}])