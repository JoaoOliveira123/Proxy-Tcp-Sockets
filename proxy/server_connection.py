from threading import Thread
import socket

from .proxy_interfaces import IServerConnectionProxy

class ProxyClient(IServerConnectionProxy):    
    def start_connection(self, host: str, port: int):
        proxy_thread = Thread(target=self.start_connection_with_server, args=(host, port))

        proxy_thread.start()
    
    def start_connection_with_server(self, host: str, port: int):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
