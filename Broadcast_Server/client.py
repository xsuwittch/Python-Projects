import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8000))

try:
    while True:
        data = client_socket.recv(4096)
        if not data:
            print("Server closed the connection")
            break
        print(data.decode())
finally:
    client_socket.close()