from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH

def route_dns(domain):
    run_cmd([CLOUDFLARED_PATH, "tunnel", "route", "dns", "alexa-tunnel", domain], True)
