import subprocess
import logging
import os
from src.utils.PATHS import CLOUDFLARED_PATH, USER_CONFIG_FILES_DIR
from src.utils.tunnel_data import tunnel_name

def delete_tunnel_background():
    try:
        cloudflared = f'"{CLOUDFLARED_PATH}"'

        log_path = os.path.join(USER_CONFIG_FILES_DIR, "uninstall.log")
        
        cmd = (
            f'timeout /t 50 >nul && '
            f'{cloudflared} tunnel delete {tunnel_name} '
            f'>> "{log_path}" 2>&1'
        )

        subprocess.Popen(
            cmd,
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        logging.info(f"Scheduled tunnel deletion in background -> {log_path}")
        
    except Exception:
        logging.exception("Failed to schedule tunnel deletion")