import socket
import ssl


class EPPClient:
    """Client per la comunicazione con server EPP tramite HTTP POST su SSL"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session_cookie = None
    
    def send_request(self, xml_content):
        """Invia una richiesta EPP tramite HTTP POST su SSL"""
        # Crea connessione SSL
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = context.wrap_socket(sock, server_hostname=self.host)
        ssl_sock.connect((self.host, self.port))
        ssl_sock.settimeout(10)
        
        # Costruisci richiesta HTTP POST
        http_request = f'POST / HTTP/1.1\r\n'
        http_request += f'Host: {self.host}\r\n'
        
        # Aggiungi cookie di sessione se presente
        if self.session_cookie:
            http_request += f'Cookie: {self.session_cookie}\r\n'
        
        http_request += 'Referer: EPP Client Test\r\n'
        http_request += 'Content-type: application/x-www-form-urlencoded\r\n'
        http_request += f'Content-length: {len(xml_content)}\r\n'
        http_request += 'Connection: close\r\n'
        http_request += '\r\n'
        http_request += xml_content
        
        # Invia richiesta
        ssl_sock.sendall(http_request.encode('utf-8'))
        
        # Leggi risposta
        response = b''
        while True:
            try:
                chunk = ssl_sock.recv(4096)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                break
        
        ssl_sock.close()
        
        # Decodifica risposta
        response_text = response.decode('utf-8', errors='ignore')
        
        # Estrai cookie Set-Cookie dalla risposta
        if 'Set-Cookie: ' in response_text:
            cookie_start = response_text.find('Set-Cookie: ') + len('Set-Cookie: ')
            cookie_end = response_text.find(';', cookie_start)
            self.session_cookie = response_text[cookie_start:cookie_end]
        
        return response_text
    
    def is_logged_in(self):
        """Verifica se c'è una sessione attiva"""
        return self.session_cookie is not None
