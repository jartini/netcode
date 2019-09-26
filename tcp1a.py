import socket
import threading

class server:

    MAX = 2

    def __init__(self, host, port, tcp = True):
        self.host = host
        self.port = port
        self.type = tcp
        self.server = self.__server()
        self.server_routine()

    def __init__(self, port, tcp = True):
        self.host = socket._LOCALHOST
        self.port = port
        self.type = tcp
        self.__server()
        self.server_routine()

    def __server(self):
        server = socket.socket()
        if self.type == True:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            server.bind((self.host, self.port))
        except:
            exit()
        server.listen(self.MAX)
        print("[**]\tLISTENING\t{0}:{1}".format(self.host, self.port))
        self.server = server

    
    def server_routine(self):

        def handler(csock):
            req = csock.recv(1024)
            print("recv:\t{0}".format(req))
            csock.send(b'ACK!')
            csock.close()
            print("CLOSED")

        while True:
            client, addr = self.server.accept()
            print("[**]\taccepted\t{0}:{1}".format(addr[0], addr[1]))
            thread = threading.Thread(
                target = handler,
                args = (client,)
            )
            thread.start()
        exit()






if __name__ == "__main__":
    server(9999)