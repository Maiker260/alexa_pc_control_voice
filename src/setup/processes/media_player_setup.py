from .media_player.install_mpv import install_mpv
from .media_player.install_yt_dlp import install_yt_dlp

def media_player_setup(write):
    write("Installing MPV...")
    install_mpv()

    write("Installing yt-dlp...")
    install_yt_dlp()

    write("Cloudflared setup done.")