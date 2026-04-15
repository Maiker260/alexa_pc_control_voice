import subprocess
import signal

class Player:
    def __init__(self):
        self.process = None

    def play_stream(self, song):
        self.stop()

        self.process = subprocess.Popen(
            ["mpv", f"ytdl://ytsearch:{song}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def pause(self):
        if self.process:
            self.process.send_signal(signal.SIGSTOP)

    def resume(self):
        if self.process:
            self.process.send_signal(signal.SIGCONT)

    def get_state(self):
        if not self.process:
            return "stopped"
        return self.process.poll()