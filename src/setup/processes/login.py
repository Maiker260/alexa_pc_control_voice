from .run import run
from .cloudflare_process import CLOUDFLARED

def login():
    print("Opening Cloudflare Login...")
    run(f"{CLOUDFLARED} tunnel login")