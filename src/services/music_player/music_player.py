import threading
import time

from .queue_manager import QueueManager
from .player import Player
from src.utils.get_playlist_urls import get_playlist_urls

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
            self.running = True
            self.thread = threading.Thread(target=self.loop, daemon=True)
            self.thread.start()

    def play(self, song):
        print("Playing Music...")
        with self.lock:
            self.queue.add(song)

        self.ensure_thread()

    def play_playlist(self, playlist_url):
        print("Loading playlist...")

        urls = get_playlist_urls(playlist_url)

        with self.lock:
            for url in urls:
                self.queue.add(url)

        self.ensure_thread()

    def volume_control(self, vol_action, vol_value):
        self.player.volume_control(vol_action, vol_value)

    def skip(self):
        self.player.stop()
        self.playing = False

    def pause(self):
        print("Pausing the Music...")
        self.player.pause()

    def resume(self):
        print("Resuming the Music...")
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