import yaml

class IPFilter:
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
            self.blocked_ips = config.get("blocked_ips", [])

    def is_blocked(self, ip):
        return ip in self.blocked_ips
