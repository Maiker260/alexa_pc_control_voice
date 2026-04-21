import subprocess
from src.utils.run_ps import run_ps

def uninstall_media_tools():
    try:
        run_ps('winget uninstall --id mpv-player.mpv-CI.MSVC --exact --silent')
        run_ps('winget uninstall --id yt-dlp.yt-dlp --exact --silent')
        run_ps('winget uninstall --id yt-dlp.FFmpeg --exact --silent')
        print("Media tools removed successfully.")
    except subprocess.CalledProcessError:
        print("MPV and/or yt-dlp not installed or already removed.")