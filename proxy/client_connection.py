import sys

from .proxy_interfaces import IProxy

class ProxyServer(IProxy):
    def start_connection(self, clients_accepted: int):
        try:
            self.__build_server(clients_accepted)
        except:
            self.__start_server_listening_error()

    def __build_server(self, clients_accepted: int):
        self.server.bind(self.address)
        self.__print_server_is_listening()
        self.server.listen(clients_accepted)

    def __print_server_is_listening(self):
        print('[*] Listening on %s:%d' % self.address)

    def __start_server_listening_error(self):
        print("[!!] Failed to listen on %s:%d" % self.local_address)
        print('[!!] Check for other listening sockets or correct permissions')
        sys.exit(0)