from abc import ABC, abstractmethod

class IRequestDataHandler(ABC):
    @abstractmethod
    def handle_request(self, buffer: bytes):


        raise NotImplementedError()


class IResponseDataHandler(ABC):
    @abstractmethod
    def handle_response(self, buffer: bytes):


        raise NotImplementedError()


class IOrganizedDumper(ABC):
    @abstractmethod
    def dump(self, src, length: int):
        

        raise NotImplementedError()

class IUnorganizedDumper(ABC):
    @abstractmethod
    def dump(self, src):
        pass