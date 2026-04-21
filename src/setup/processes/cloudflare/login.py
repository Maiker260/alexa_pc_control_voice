from src.utils.run_cmd import run_cmd
from src.utils.PATHS import CLOUDFLARED_PATH

def login():
    print("Opening Cloudflare Login...")
    run_cmd([CLOUDFLARED_PATH, "tunnel", "login"])