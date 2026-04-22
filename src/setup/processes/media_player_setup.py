from .media_player.install_mpv import install_mpv
from .media_player.install_yt_dlp import install_yt_dlp
from src.utils.is_installed import is_installed

def media_player_setup(write):
    if not is_installed("mpv"):
        write("Installing MPV...")
        install_mpv()

    if not is_installed("yt-dlp"):
        write("Installing yt-dlp...")
        install_yt_dlp()

    write("Media Player setup done.")