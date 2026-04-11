from .run import run
from .cloudflare_process import CLOUDFLARED

def create_tunnel():
    run(f"{CLOUDFLARED} tunnel create alexa-tunnel")