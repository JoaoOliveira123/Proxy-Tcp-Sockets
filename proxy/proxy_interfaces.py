from abc import ABC, abstractmethod
import socket

class IProxy(ABC):
    @abstractmethod
    def start_connection(self, *args, **kwargs):


        raise NotImplementedError()


class IClientConnectionProxy(IProxy):
    def __init__(self, host: str, port: int):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.local_address = (host, port)

class IServerConnectionProxy(IProxy):
    pass

class IProxyManager(ABC):
    def __init__(self, local_host: str, local_port: int, remote_host: str, remote_port: int):
        self.local_host = local_host
        self.local_port = local_port
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.local_address = (local_host, local_port)
        self.remote_address = (remote_host, remote_port)
    
    @abstractmethod
    def start_server_for_client(self):


        raise NotImplementedError()
    
    @abstractmethod
    def start_connection_to_server(self):


        raise NotImplementedError()