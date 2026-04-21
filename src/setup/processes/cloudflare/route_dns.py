from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH
import subprocess

def route_dns(domain, log):
    try:
        run_cmd([CLOUDFLARED_PATH, "tunnel", "route", "dns", "alexa-tunnel", domain])
        log("DNS created")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr or e.stdout or ""

        if "already exists" in error_msg or "code: 1003" in error_msg:
            log("DNS already exists, using previous config.")
        else:
            log(f"DNS Error: {error_msg}")
            raise