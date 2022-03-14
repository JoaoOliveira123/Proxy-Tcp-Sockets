import socket
import pexpect
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
max_time = 2
server.bind(('localhost', 5000))
server.listen(1)
minnimum_time = 0,2

while minnimum_time < max_time:
    server.settimeout(minnimum_time)
    sock, addr = server.accept()
    minnimum_time *= 2