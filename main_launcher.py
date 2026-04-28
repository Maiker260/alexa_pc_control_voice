import ctypes
import sys
import logging
import multiprocessing

from src.main_launcher.start_services import start_services
from src.main_launcher.create_icon import create_icon
from src.utils.setup_logging import setup_logging, setup_uvicorn_logging

# Start Logging
setup_logging("launcher.log", level=logging.INFO)
setup_uvicorn_logging()

# Avoid to run the app twice.
mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "AlexaPC_MUTEX")

if ctypes.windll.kernel32.GetLastError() == 183:
    logging.info("App already running")
    sys.exit(0)

def main():
    start_services()
    create_icon()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()