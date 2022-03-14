from .utils_interfaces import IRequestDataHandler
from .utils_interfaces import IResponseDataHandler
from .utils_interfaces import IDumper

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
class BytesToHexOrganizedDumper(IDumper):
    def dump(self, src: bytes, length: int):
        pass