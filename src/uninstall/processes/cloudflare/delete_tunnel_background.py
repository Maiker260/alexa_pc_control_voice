import subprocess
import logging
from src.utils.PATHS import CLOUDFLARED_PATH
from src.utils.tunnel_data import tunnel_name

def delete_tunnel_background():
    try:
        cloudflared = f'"{CLOUDFLARED_PATH}"'
        cmd = (
            f'timeout /t 50 >nul && '
            f'{cloudflared} tunnel delete {tunnel_name} '
            f'>> "%APPDATA%\\AlexaPcVoiceControl\\uninstall.log" 2>&1'
        )

        subprocess.Popen(
            cmd,
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        logging.info("Scheduled tunnel deletion in background")
    except Exception:
        logging.exception("Failed to schedule tunnel deletion")