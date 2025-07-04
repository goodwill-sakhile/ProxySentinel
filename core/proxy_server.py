import socket
import threading
from core.traffic_interceptor import TrafficInterceptor

class ProxyServer:
    """
    The ProxyServer class listens for HTTP connections
    and passes traffic to the TrafficInterceptor.
    """
    def __init__(self, rule_engine, host='0.0.0.0', port=8080):
        self.rule_engine = rule_engine
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.interceptor = TrafficInterceptor(rule_engine)

    def start(self):
        """
        Starts the proxy server in a multi-threaded mode.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(100)
        print(f"[INFO] Proxy server running on {self.host}:{self.port}")

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"[INFO] Incoming connection from {client_address}")
                client_thread = threading.Thread(
                    target=self.handle_client, args=(client_socket, client_address))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("[INFO] Shutting down proxy server.")
            self.server_socket.close()

    def handle_client(self, client_socket, client_address):
        """
        Handles a single client connection.
        """
        self.interceptor.intercept(client_socket, client_address)

