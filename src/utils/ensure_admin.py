import ctypes
import sys
import os
from src.utils.show_popup import show_popup

def ensure_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return

    show_popup(
        "The application will restart with administrator privileges.",
        "Permission Required",
    )

    params = " ".join([f'"{arg}"' for arg in sys.argv])
    
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        params,
        None,
        1
    )

    os._exit(0)