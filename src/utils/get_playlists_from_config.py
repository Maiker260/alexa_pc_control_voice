import json
import logging

from src.utils.ensure_playlist_file import ensure_playlist_file

def get_playlists_from_config(playlist_kwd):
    playlist_path = ensure_playlist_file()

    try:
        with open(playlist_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        logging.exception("Invalid playlists.json")
        return None

    if not isinstance(data, list):
        logging.error("playlists.json must contain a list")
        return None

    playlist_kwd = playlist_kwd.lower().strip()

    for item in data:
        keywords = item.get("keywords", [])
        url = item.get("url")
        
        if not keywords or not url:
            continue

        if any(keyword.lower() == playlist_kwd for keyword in keywords):
            logging.info(f"Keyword '{playlist_kwd}' matched playlist: {url}")
            return url
        
    logging.info("No playlist match found")

    return None