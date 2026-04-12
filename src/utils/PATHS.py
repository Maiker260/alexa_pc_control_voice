import os

CLOUDFLARED_PATH = r"C:\Program Files (x86)\cloudflared\cloudflared.exe"
CLOUDFLARED_DIR = r"C:\Program Files (x86)\cloudflared"
USER_DATA_DIR = os.path.join(os.environ["USERPROFILE"], ".cloudflared")
USER_CONFIG_FILES_DIR = os.path.join(os.environ["USERPROFILE"], ".alexaPcVoiceControl")