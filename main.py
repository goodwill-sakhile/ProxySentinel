from core.proxy_server import ProxyServer
from core.rule_engine import RuleEngine

def main():
    print("[INFO] Starting Python Web Filter...")
    rule_engine = RuleEngine()
    proxy = ProxyServer(rule_engine)
    proxy.start()

if __name__ == "__main__":
    main()
