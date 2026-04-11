from .run import run
from utils.PATHS import CLOUDFLARED_PATH

def route_dns(domain):
    run(f'"{CLOUDFLARED_PATH}" tunnel route dns alexa-tunnel {domain}')