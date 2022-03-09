from abc import ABC, abstractmethod
import socket

class IProxy(ABC):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.address = (host, port)

    @abstractmethod
    def start_connection(self, *args, **kwargs):


        raise NotImplementedError()

class IProxyDataManager(ABC):    
    @abstractmethod
    def start_data_flow(self, proxy_server: socket.socket, proxy_client: socket.socket):


        raise NotImplementedError()