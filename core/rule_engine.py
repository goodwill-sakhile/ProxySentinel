from filters.ip_filter import IPFilter
from filters.keyword_filter import KeywordFilter

class RuleEngine:
    def __init__(self):
        self.ip_filter = IPFilter()
        self.keyword_filter = KeywordFilter()

    def should_block(self, ip, url):
        if self.ip_filter.is_blocked(ip):
            return True
        if self.keyword_filter.is_blocked(url):
            return True
        return False
