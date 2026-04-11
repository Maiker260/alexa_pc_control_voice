import subprocess
import time
from .utils.tunnel_data import tunnel_name
from .utils.PATHS import CLOUDFLARED_PATH

def start_services():
    print("Starting Services...")

    subprocess.Popen("uvicorn main:app --host 0.0.0.0 --port 8000", shell=True)
    time.sleep(5)
    subprocess.Popen(f'"{CLOUDFLARED_PATH}" tunnel run {tunnel_name}', shell=True)

if __name__ == "__main__":
    start_services()