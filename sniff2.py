from socket import *
from sys import platform, exit

class sniffer:

    def __init__(self, interface, port):
        self.port = port
        self.interface = interface
        self.run()

    def __init__(self, interface):
        self.port = 0
        self.interface = interface
        self.run()

    def __init__(self):
        self.run()

    def __createRawSocketWindows(self):
        try:
            self.s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
            self.s.bind((
                self.interface,
                self.port
            ))
            self.s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
            self.s.ioctl(SIO_RCVALL, RCVALL_ON)
        except error:
            print("EXCEPTION:\t{0}".format(error))
            sys.exit()

    def __createRawSocketUnix(self):
        
        try:
            self.s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
        except error:
            print("EXCEPTION:\t{0}".format(error))
            sys.exit()

    def __create_socket(self):
        if "win" in platform.lower():
            self.__createRawSocketWindows()
        else:
            self.__createRawSocketUnix()        

    def getAndParse(self):

        def get_packets(self):
            return self.s.recvfrom(4096)

        def packet_decontructor(data):
            return

        packet = self.get_packets()
        return packet_decontructor(packet[0]), packet[1]
        
    def run(self):
        self.__create_socket()