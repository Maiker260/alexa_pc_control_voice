import subprocess
import logging
from src.utils.run_ps import run_ps

def remove_user_config():
    try:
        run_ps(
            'if (Test-Path $env:USERPROFILE\\.cloudflared) { Remove-Item -Recurse -Force $env:USERPROFILE\\.cloudflared }'
        )
        logging.info("User config removed successfully.")
    except subprocess.CalledProcessError:
        logging.info("User config already removed.")