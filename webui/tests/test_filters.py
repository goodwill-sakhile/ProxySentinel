from filters.ip_filter import IPFilter
from filters.keyword_filter import KeywordFilter

def test_ip_filter():
    ip_filter = IPFilter()
    assert ip_filter.is_blocked("192.168.1.10") == True
    assert ip_filter.is_blocked("8.8.8.8") == False

def test_keyword_filter():
    keyword_filter = KeywordFilter()
    assert keyword_filter.is_blocked("http://example.com/adult") == True
    assert keyword_filter.is_blocked("http://example.com/normal") == False
