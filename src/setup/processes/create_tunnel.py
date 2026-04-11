from .run import run
from .cloudflare_process import CLOUDFLARED

def create_tunnel(tunnel_name):
    run(f"{CLOUDFLARED} tunnel create {tunnel_name}")