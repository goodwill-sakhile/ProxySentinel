import scapy.all as scapy
from scapy.layers.http import HTTPRequest

class TrafficInterceptor:
    def __init__(self, rule_engine):
        self.rule_engine = rule_engine

    def start(self):
        print("[INFO] Intercepting HTTP traffic...")
        scapy.sniff(filter="tcp port 80", prn=self.process_packet, store=False)

    def process_packet(self, packet):
        if packet.haslayer(HTTPRequest):
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            ip = packet[scapy.IP].src
            if self.rule_engine.should_block(ip, url):
                print(f"[BLOCKED] {ip} tried accessing {url}")
