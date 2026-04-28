import subprocess
import logging
from src.utils.run_ps import run_ps

def uninstall_media_tools():
    try:
        run_ps('winget uninstall --id mpv-player.mpv-CI.MSVC --exact --silent')
        run_ps('winget uninstall --id yt-dlp.yt-dlp --exact --silent')
        run_ps('winget uninstall --id yt-dlp.FFmpeg --exact --silent')
        logging.info("Media tools removed successfully.")
    except subprocess.CalledProcessError:
        logging.info("MPV and/or yt-dlp not installed or already removed.")