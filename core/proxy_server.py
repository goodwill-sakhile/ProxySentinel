import socketserver
from core.traffic_interceptor import TrafficInterceptor

class ProxyServer:
    def __init__(self, rule_engine):
        self.rule_engine = rule_engine

    def start(self):
        print("[INFO] Proxy server is running...")
        interceptor = TrafficInterceptor(self.rule_engine)
        interceptor.start()
