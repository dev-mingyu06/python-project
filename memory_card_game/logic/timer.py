import time

class Timer:
    def __init__(self, limit):
        self.limit = limit
        self.start_time = time.time()

    def time_left(self):
        return max(0, self.limit - int(time.time() - self.start_time))

    def is_time_up(self):
        return self.time_left() <= 0