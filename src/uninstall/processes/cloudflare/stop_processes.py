import subprocess
import logging
import time

def stop_processes():
    processes = [
        "AlexaPcVoiceControl.exe",
        "cloudflared.exe"
    ]

    for proc in processes:
        try:
            subprocess.run(
                ["taskkill", "/F", "/T", "/IM", proc],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            logging.info(f"Terminated {proc}")
        except Exception:
            logging.exception(f"Failed to terminate {proc}")

    time.sleep(2)