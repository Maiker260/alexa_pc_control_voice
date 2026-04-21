import ctypes
import sys
import os

def ensure_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return

    ctypes.windll.user32.MessageBoxW(
        0,
        "The application will restart with administrator privileges.",
        "Permission Required",
        0x40
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