import socket
import threading

bindIP = socket._LOCALHOST
bindPort = 9999

#create socket
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

#bind socket
server.bind(
    (
        bindIP,
        bindPort
    )
)

server.listen(5) #max port connection of 5

print("[**]\tLISTENING {0}:{1}".format(bindIP, bindPort))

def handler(client):

    req = client.recv(1024)
    #receive 1024 bytes

    print("[**]\tRECV: {0}".format(req))

    client.send(b'ACK!')

    client.close()

while True:
    client, addr = server.accept()
     
    print("[**]\tAccpeted Conn:{0}:{1}".format(addr[0], addr[1]))

    handler(client)