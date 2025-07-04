import datetime

class ActivityLogger:
    """
    Logs blocked and allowed requests.
    """
    def __init__(self, logfile="logs/blocked_requests.log"):
        self.logfile = logfile

    def log(self, ip, url, action="BLOCKED"):
        with open(self.logfile, "a") as f:
            f.write(f"{datetime.datetime.now()}: {action} {ip} -> {url}\n")

