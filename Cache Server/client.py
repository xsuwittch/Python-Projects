import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',8000))

request = "GET /random.txt HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n"

client_socket.sendall(request.encode())

respone = b""

while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    respone += chunk

print(respone.decode())
client_socket.close()