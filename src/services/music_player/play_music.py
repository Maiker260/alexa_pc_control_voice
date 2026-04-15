from .music_player import MusicPlayer

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
    }

    if music_action not in actions:
        raise ValueError(f"Invalid music action: {music_action}")

    if music_action == "play":
        if not song:
            raise ValueError("Missing song_name")

        actions[music_action](song)
        return {"message": f"Added: {song}"}

    else:
        actions[music_action]()
        return {"message": f"{music_action} executed"}