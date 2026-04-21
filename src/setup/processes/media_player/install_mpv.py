from src.utils.run_ps import run_ps

def install_mpv():
    print("Installing MPV...")
    run_ps("winget install --id mpv-player.mpv-CI.MSVC --exact --accept-source-agreements --accept-package-agreements --silent", True)