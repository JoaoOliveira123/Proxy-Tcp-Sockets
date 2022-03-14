from abc import ABC, abstractmethod
from typing import Union, Type

from .utils_interfaces import IUnorganizedDumper, IOrganizedDumper

class IProxy(ABC):
    def __init__(self, host: str, port: int, 
                dumper: Union[Type[IUnorganizedDumper], Type[IOrganizedDumper]]):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dumper = dumper

    @abstractmethod
    def start_connection(self, *args, **kwargs):


        raise NotImplementedError


class IProxyDataManager(ABC):    
    @abstractmethod
    def start_data_flow(self, proxy_server: IProxy, proxy_client: IProxy):


        raise NotImplementedError()