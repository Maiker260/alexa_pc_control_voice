from .run import run
from src.utils.PATHS import CLOUDFLARED_PATH

def login():
    print("Opening Cloudflare Login...")
    run([CLOUDFLARED_PATH, "tunnel", "login"])