from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH
import subprocess

def route_dns(domain, log):
    try:
        run_cmd([CLOUDFLARED_PATH, "tunnel", "route", "dns", "alexa-tunnel", domain])
        log("DNS created")
    except subprocess.CalledProcessError as e:
        if "already exists" in (e.stderr or ""):
            log("DNS already exists, using previous config.")
        else:
            log(f"DNS Error: {e}")
            raise