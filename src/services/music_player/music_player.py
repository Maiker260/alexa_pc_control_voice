import threading
import time
import vlc

from .yt_manager import get_stream
from .queue_manager import QueueManager
from .player import Player

class MusicPlayer:
    def __init__(self):
        self.queue = QueueManager()

        self.player = Player()
        self.playing = False

        self.thread = None
        self.lock = threading.Lock()
        self.running =  False

    def loop(self):
        while self.running:
            song = None

            with self.lock:
                if not self.playing:
                    song = self.queue.get_next()

            if song:
                self.player.play_stream(song)
                self.playing = True

            if self.player.process and self.player.process.poll() is not None:
                self.playing = False
                self.player.process = None

            time.sleep(0.5)

    def ensure_thread(self):
        if self.thread is None or not self.thread.is_alive():
            print("Starting thread")
            self.running = True
            self.thread = threading.Thread(target=self.loop, daemon=True)
            self.thread.start()

    def play(self, song):
        with self.lock:
            self.queue.add(song)

        self.ensure_thread()

    def skip(self):
        self.player.stop()
        self.playing = False

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()

    def stop(self):
        print("Stopping Music...")

        with self.lock:
            self.queue.queue.clear()
            self.playing = False

        if self.player:
            self.player.stop()

        self.running = False

        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2)

        self.thread = None