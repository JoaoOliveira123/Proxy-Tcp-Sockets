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
    digits = 2

    def __init__(self):
        self.__result = []

    def dump(self, src: bytes, line_length: int=16):
        for i in self.hexdump(src, line_length):
            self.__result.append(i)
    
    def hexdump(self, src: bytes, line_length: int=16):
        for i in range(0, len(src), line_length):
            s = src[i:i+line_length]
            hexa = b' '.join([b'%0*X' % (self.digits, x) for x in s])
            text = b''.join([x if 0x20 <= ord(x) < 0x7f else b'.' for x in s])
            yield b'%04X  %-*s  %s' % (i, line_length*(self.digits + 1), hexa, text)
    
    @property
    def result(self):
        return self.__result
    
    def print_hexa_value(self):
        print(b'\n'.join(self.result).decode())