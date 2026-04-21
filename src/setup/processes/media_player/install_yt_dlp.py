from src.utils.run_ps import run_ps

def install_yt_dlp():
    print("Installing yt-dlp...")
    run_ps("winget install --id yt-dlp.yt-dlp --exact --accept-source-agreements --accept-package-agreements --silent")
