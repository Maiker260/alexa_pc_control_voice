import subprocess

from src.utils.send_music_command import send_music_command

class Player:
    def __init__(self):
        self.process = None

    def play_stream(self, song):
        self.stop()

        self.process = subprocess.Popen(
            [
                "mpv", 
                r"--input-ipc-server=\\.\pipe\mpvsocket", 
                "--volume=60",
                f"ytdl://ytsearch:{song}", 
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    
    def volume_control(self, vol_action, vol_value):
        if vol_value is None:
            vol_value = 5

        actions = {
            "vol_up": ["add", "volume", vol_value],
            "vol_down": ["add", "volume", -vol_value],
            "set_vol": ["set", "volume", vol_value]
        }

        if self.process:
            if vol_action in actions:
                command = actions[vol_action]
            else:
                raise ValueError("Invalid action: use 'vol_up', 'vol_down' or 'set_vol'")

            return send_music_command(command)

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def pause(self):
        if self.process:
            return send_music_command(["set", "pause", True])

    def resume(self):
        if self.process:
            return send_music_command(["set", "pause", False])
    
    