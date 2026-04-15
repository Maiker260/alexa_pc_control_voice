# import vlc

# class Player:
#     def __init__(self):
#         self.player = None

#     def play_stream(self, url):
#         self.player = vlc.MediaPlayer(url)
#         self.player.play()

#     def stop(self):
#         if self.player:
#             self.player.stop()

#     def pause(self):
#         if self.player:
#             self.player.pause()

#     def resume(self):
#         if self.player:
#             self.player.play()

#     def get_state(self):
#         if self.player:
#             return self.player.get_state()
#         return None

import subprocess

class Player:
    def __init__(self):
        self.process = None

    def play_stream(self, url):
        self.stop()

        # self.process = subprocess.Popen(
        #     ["mpv", url],
        #     # stdout=subprocess.DEVNULL,
        #     # stderr=subprocess.DEVNULL
        # )
        self.process = subprocess.Popen(
            ["mpv", url],
            stderr=subprocess.PIPE,
            text=True
        )

        for line in self.process.stderr:
            print("[mpv ERROR]", line.strip())

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None

    def pause(self):
        if self.process:
            self.process.send_signal(19)  # SIGSTOP

    def resume(self):
        if self.process:
            self.process.send_signal(18)  # SIGCONT

    def get_state(self):
        if not self.process:
            return "stopped"
        return self.process.poll()