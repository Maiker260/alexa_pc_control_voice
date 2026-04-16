from .music_player import MusicPlayer
from src.utils.parse_num import parse_num

music_player = MusicPlayer()

def play_music(data):
    music_action = data.get("music_action", "")
    song = data.get("song_name", "")

    actions = {
        "play": music_player.play,
        "skip": music_player.skip,
        "pause": music_player.pause,
        "resume": music_player.resume,
        "stop": music_player.stop,
        "volume": music_player.volume_control
    }

    if music_action not in actions:
        raise ValueError(f"Invalid music action: {music_action}")

    if music_action == "play":
        if not song:
            raise ValueError("Missing song_name")

        actions[music_action](song)
        return {"message": f"Added: {song}"}
    
    elif music_action == "volume":
        vol_action= data.get("vol_action", "")
        vol_value = parse_num(data.get("vol_value", 0))

        actions[music_action](vol_action, vol_value)
        return {"message": f"Volume {vol_action}"}

    else:
        actions[music_action]()
        return {"message": f"{music_action} executed"}