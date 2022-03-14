from .utils_interfaces import IRequestDataHandler
from .utils_interfaces import IResponseDataHandler
from .utils_interfaces import IOrganizedDumper

#Just copy the data of request
class RequestDataCopier(IRequestDataHandler):
    def handle_request(self, buffer: bytes):
        # In other classes, make changes and verifications
        return buffer

class ResponseDataCopier(IResponseDataHandler):
    def handle_response(self, buffer: bytes):
        # In other classes, make changes and verifications
        return buffer

#Organized is why it 
class BytesToHexOrganizedDumper(IOrganizedDumper):
    def dump(self, src: bytes, length: int):
        future_result = []
        digits = 2
        for i in range(0, len(src), length):
            future_result.append(self.hexdump_bytes(src, digits))