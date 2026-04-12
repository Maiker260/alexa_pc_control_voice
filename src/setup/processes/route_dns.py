from .run import run
from src.utils.PATHS import CLOUDFLARED_PATH

def route_dns(domain):
    run([CLOUDFLARED_PATH, "tunnel", "route", "dns", "alexa-tunnel", {domain}])
