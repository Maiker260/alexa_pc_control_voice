import os

from src.main_launcher import start_services

def on_exit(icon, item):
    print("Shutting down...")

    if start_services.process:
        start_services.process.terminate()
        start_services.process.wait(timeout=5)

    icon.stop()
    os._exit(0)