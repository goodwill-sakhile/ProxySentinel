import select

class TrafficInterceptor:
    """
    Intercepts HTTP traffic and applies the rule engine.
    """
    def __init__(self, rule_engine):
        self.rule_engine = rule_engine

    def intercept(self, client_socket, client_address):
        """
        Handles the data stream between client and remote server.
        """
        request = client_socket.recv(8192)
        first_line = request.split(b'\n')[0]
        url = first_line.split()[1]

        http_pos = url.find(b"://")
        temp = url[(http_pos + 3):] if http_pos != -1 else url
        port_pos = temp.find(b":")
        webserver_pos = temp.find(b"/")

        webserver = ""
        port = -1
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = temp[:webserver_pos]
        port = 80 if port_pos == -1 or webserver_pos < port_pos else int(temp[port_pos+1:webserver_pos])

        ip = client_address[0]

        # Apply block rules
        if self.rule_engine.should_block(ip, url.decode()):
            print(f"[BLOCKED] {ip} tried accessing {url.decode()}")
            client_socket.close()
            return

        # Connect to destination
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((webserver.decode(), port))
            s.send(request)

            while True:
                ready = select.select([s], [], [], 3)
                if ready[0]:
                    data = s.recv(8192)
                    if len(data) > 0:
                        client_socket.send(data)
                    else:
                        break
            s.close()
            client_socket.close()
        except socket.error as e:
            print(f"[ERROR] {e}")
            s.close()
            client_socket.close()
