import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    max_time = 2
    server.bind(('localhost', 5000))
    server.listen(1)
    minnimum_time = 0.2

    while minnimum_time < max_time:
        server.settimeout(minnimum_time)
        try:
            sock, addr = server.accept()
        except:
            break
        minnimum_time *= 2