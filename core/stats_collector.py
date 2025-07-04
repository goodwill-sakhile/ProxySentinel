import threading
import time

class StatsCollector:
    """
    Collects statistics about allowed and blocked requests.
    """
    def __init__(self):
        self.total_requests = 0
        self.blocked_requests = 0
        self.allowed_requests = 0
        self.lock = threading.Lock()

    def increment_total(self):
        with self.lock:
            self.total_requests += 1

    def increment_blocked(self):
        with self.lock:
            self.blocked_requests += 1

    def increment_allowed(self):
        with self.lock:
            self.allowed_requests += 1

    def log_stats(self):
        while True:
            time.sleep(60)
            print(f"[STATS] Total: {self.total_requests}, "
                  f"Blocked: {self.blocked_requests}, "
                  f"Allowed: {self.allowed_requests}")
