class URLFilter:
    """
    Provides pattern-based URL filtering.
    """
    def __init__(self):
        self.blocked_domains = ["badwebsite.com", "bannedsite.org"]

    def is_blocked(self, url):
        for domain in self.blocked_domains:
            if domain in url.lower():
                return True
        return False
