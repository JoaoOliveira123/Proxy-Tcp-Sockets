from .proxy_interfaces import IClientConnectionProxy
from .proxy_interfaces import IServerConnectionProxy
from .proxy_interfaces import IProxyManager

class ProxyReicevingDataManager(IProxyManager):
    def start_server_for_client(self, server_of_proxy: IClientConnectionProxy):
        server_of_proxy.start_connection(self.remote_host, self.remote_port)