import subprocess
import time
from .setup.processes.cloudflare_process import CLOUDFLARED
from .utils.tunnel_data import tunnel_name

def start_services():
    print("Starting Services...")

    subprocess.Popen("uvicorn main:app --host 0.0.0.0 --port 8000", shell=True)
    time.sleep(5)
    subprocess.Popen(f"{CLOUDFLARED} tunnel run {tunnel_name}", shell=True)

if __name__ == "__main__":
    start_services()