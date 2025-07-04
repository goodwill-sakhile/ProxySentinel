import datetime

class ActivityLogger:
    def __init__(self, logfile="blocked_requests.log"):
        self.logfile = logfile

    def log(self, ip, url):
        with open(self.logfile, "a") as f:
            f.write(f"{datetime.datetime.now()}: BLOCKED {ip} -> {url}\n")
