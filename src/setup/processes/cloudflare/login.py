from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH

def login():
    try:
        print("Opening Cloudflare Login...")
        run_cmd([CLOUDFLARED_PATH, "tunnel", "login"])
    except:
        print("Unable to login into Cloudflare website...")