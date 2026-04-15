import vlc

class Player:
    def __init__(self):
        self.player = None

    def play_stream(self, url):
        self.player = vlc.MediaPlayer(url)
        self.player.play()

    def stop(self):
        if self.player:
            self.player.stop()

    def pause(self):
        if self.player:
            self.player.pause()

    def resume(self):
        if self.player:
            self.player.play()

    def get_state(self):
        if self.player:
            return self.player.get_state()
        return None