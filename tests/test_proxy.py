from core.rule_engine import RuleEngine

def test_should_block_ip():
    engine = RuleEngine()
    assert engine.should_block("192.168.1.10", "http://example.com") == True

def test_should_block_keyword():
    engine = RuleEngine()
    assert engine.should_block("8.8.8.8", "http://example.com/adult") == True

def test_should_allow():
    engine = RuleEngine()
    assert engine.should_block("8.8.8.8", "http://example.com/normal") == False
