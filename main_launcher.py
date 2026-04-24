import threading
import multiprocessing
import os
from datetime import datetime

from src.main_launcher.start_services import start_services
from src.main_launcher.create_icon import create_icon

def main():
    with open("debug.log", "a") as f:
        f.write(f"{datetime.now()} PID={os.getpid()}\n")
        
    threading.Thread(target=start_services, daemon=True).start()
    create_icon()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()