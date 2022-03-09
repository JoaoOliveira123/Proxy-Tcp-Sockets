import socket

from .proxy_interfaces import IProxy


class ProxyClient(IProxy):       
    def start_connection(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(self.address)
