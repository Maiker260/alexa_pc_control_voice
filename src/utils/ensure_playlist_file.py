import json
from pathlib import Path
import logging
from src.utils.PATHS import USER_CONFIG_FILES_DIR

def ensure_playlist_file():
    config_dir = Path(USER_CONFIG_FILES_DIR)
    config_dir.mkdir(parents=True, exist_ok=True)

    playlist_path = config_dir / "playlists.json"

    if playlist_path.exists():
        logging.info("playlists.json already exists")
        return playlist_path

    template = [
        {
            "_comment": "Add your playlists below. Each item supports: name, keywords, url, shuffle (true/false)"
        },
        {
            "name": "Chill Playlist",
            "keywords": ["chill", "relax", "tranquilo"],
            "url": "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID",
            "shuffle": True
        },
        {
            "name": "Happy Playlist",
            "keywords": ["feliz", "alegre", "dia bueno"],
            "url": "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID",
            "shuffle": True
        }
    ]

    try:
        with open(playlist_path, "w", encoding="utf-8") as f:
            json.dump(template, f, indent=2, ensure_ascii=False)
        logging.info(f"Created playlists.json template at {playlist_path}")
    except Exception:
        logging.exception("Failed to create playlists.json")

    return playlist_path