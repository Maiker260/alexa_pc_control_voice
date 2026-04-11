from .run import run
from utils.PATHS import CLOUDFLARED_PATH

def login():
    print("Opening Cloudflare Login...")
    run(f'"{CLOUDFLARED_PATH}" tunnel login')