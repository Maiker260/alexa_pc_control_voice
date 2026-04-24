import os
from .process_manager import process

def on_exit(icon, item):
    print("Shutting down...")

    if process:
        try:
            process.terminate()
            process.wait(timeout=5)
        except:
            process.kill()

    icon.stop()
    os._exit(0)