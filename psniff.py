from socket import *
net = "10.127.121.182"
s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
s.bind((net,80))
s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
s.ioctl(SIO_RCVALL, RCVALL_ON)

while True:

    data, address = s.recvfrom(4096)
    if address[0] == net or address[0] == '0.0.0.0':
        continue
    else:
        print("{0}:{1}\n\n{2}\n\n".format(address[0], address[1],data))

