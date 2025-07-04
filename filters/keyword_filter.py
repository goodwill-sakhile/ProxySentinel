import yaml

class KeywordFilter:
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
            self.blocked_keywords = config.get("blocked_keywords", [])

    def is_blocked(self, url):
        for keyword in self.blocked_keywords:
            if keyword in url.lower():
                return True
        return False
