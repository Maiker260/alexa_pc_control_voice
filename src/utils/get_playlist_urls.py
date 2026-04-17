import subprocess
import time
from pathlib import Path
from .get_firefox_cookies import get_firefox_cookies

def get_playlist_urls(playlist_url):
    cookies_path = Path(get_firefox_cookies())

    if cookies_path.stat().st_mtime < (time.time() - 3600):
        cookies_path = Path(get_firefox_cookies())

    result = subprocess.run(
        [
            "yt-dlp",
            "--cookies", cookies_path,
            "--flat-playlist",
            "-g",
            playlist_url
        ],
        capture_output=True,
        text=True
    )

    return result.stdout.strip().split("\n")