from .run import run
from .cloudflare_process import CLOUDFLARED

def route_dns(domain):
    run(f"{CLOUDFLARED} tunnel route dns alexa-tunnel {domain}")