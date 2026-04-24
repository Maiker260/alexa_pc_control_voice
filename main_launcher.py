import threading

from src.main_launcher.start_services import start_services
from src.main_launcher.create_icon import create_icon

if __name__ == "__main__":
    threading.Thread(target=start_services, daemon=True).start()
    create_icon()
    