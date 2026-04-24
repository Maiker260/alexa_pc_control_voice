import ctypes
import sys
import threading
import multiprocessing

from src.main_launcher.start_services import start_services
from src.main_launcher.create_icon import create_icon

# Avoid to run the app twice.
mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "AlexaPC_MUTEX")

if ctypes.windll.kernel32.GetLastError() == 183:
    print("App already running")
    sys.exit(0)

def main():
    start_services()
    # threading.Thread(target=start_services, daemon=True).start()
    create_icon()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()