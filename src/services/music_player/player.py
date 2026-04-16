import subprocess
import signal

from src.utils.send_music_command import send_music_comand

class Player:
    def __init__(self):
        self.process = None

    def play_stream(self, song):
        self.stop()

        self.process = subprocess.Popen(
            ["mpv", f"ytdl://ytsearch:{song}", "--volume=60"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        self.process = subprocess.Popen(
            [
                "mpv", 
                "--input-ipc-server=\\.\pipe\mpvsocket", 
                "--volume=60",
                f"ytdl://ytsearch:{song}", 
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    
    def volume_control(self, vol_action, vol_value):
        vol_value = 5 if not vol_value else vol_value

        actions = {
            "vol_up": ["add", "volume", vol_value],
            "vol_down": ["add", "volume", -vol_value],
            "set": ["set", "volume", vol_value]
        }

        if self.process:
            if vol_action in actions:
                command = actions[vol_action]
            else:
                raise ValueError("Invalid action: use 'up', 'down' or 'set'")

            return send_music_comand(command)

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def pause(self):
        if self.process:
            return send_music_comand(["set", "pause", True])

    def resume(self):
        if self.process:
            return send_music_comand(["set", "pause", False])
    
    