from collections import deque

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add(self, song):
        self.queue.append(song)

    def get_next(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def get_all(self):
        return list(self.queue)