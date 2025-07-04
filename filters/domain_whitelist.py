class DomainWhitelist:
    """
    Provides domain whitelisting.
    """
    def __init__(self):
        self.allowed_domains = ["example.com", "trustedsite.org"]

    def is_allowed(self, url):
        for domain in self.allowed_domains:
            if domain in url.lower():
                return True
        return False
