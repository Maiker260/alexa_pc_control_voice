import json
from pathlib import Path

from src.utils.PATHS import USER_CONFIG_FILES_DIR

def get_playlists_from_config(playlist_kwd):
    config_dir = Path(USER_CONFIG_FILES_DIR)
    config_dir.mkdir(parents=True, exist_ok=True)

    playlist_path = config_dir / "playlists.json"
    
    if not playlist_path.exists():
        return None

    with open(playlist_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        for keyword in item.get("keywords", []):
            print(f"Keyword: {keyword}")
            if keyword.lower() in playlist_kwd:
                return item.get("url")

    return None