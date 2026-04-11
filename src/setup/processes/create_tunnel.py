from .run import run
from utils.PATHS import CLOUDFLARED_PATH

def create_tunnel(tunnel_name):
    run(f'"{CLOUDFLARED_PATH}" tunnel create {tunnel_name}')