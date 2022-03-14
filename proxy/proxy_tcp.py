from typing import Type

from .proxy_interfaces import IProxy
from .proxy_interfaces import IProxyDataManager

class ProxyDataTransmitter(IProxyDataManager):
    def start_data_flow(self, proxy_server: Type[IProxy], proxy_client: Type[IProxy]):
        pass

class ProxyWithoutData(IProxyDataManager):
    def start_data_flow(self, proxy_server: Type[IProxy], proxy_client: Type[IProxy]):
        print('Connected successfully')