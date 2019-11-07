import subprocess as sp
import socket as s


class server:

    def __init__(self, ip, port):
        server_loop(server(ip, port))

    def server(ip, port):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.bind((ip, port))
        sock.listen(50)
        return sock

    def server_loop(serv):
        while True:
            data, addr = serv.accept()

    def handler(client_sock):
        return
            