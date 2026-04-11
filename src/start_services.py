import subprocess
import time
from .setup.processes.cloudflare_process import CLOUDFLARED

def main():
    print("Starting Services...")

    subprocess.Popen("uvicorn main:app --host 0.0.0.0 --port 8000", shell=True)
    time.sleep(5)
    subprocess.Popen(f"{CLOUDFLARED} tunnel run alexa-tunnel", shell=True)

if __name__ == "__main__":
    main()