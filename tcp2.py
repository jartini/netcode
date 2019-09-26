import socket

th = 'localhost'
tp = 9999

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(
    (
        th,
        tp
    )
)

client.sendall(
    b'FUCKKKKK'
)

data, addr = client.recvfrom(4096)

print(data)