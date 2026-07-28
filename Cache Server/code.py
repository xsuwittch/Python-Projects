import socket
import argparse
from urllib import request, error
import fetchfile
parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',required=True)
parser.add_argument('-a','--address',required=True)

args = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((args.address, int(args.port)))
print(f" Socket created at {args.address} : {args.port}")

while True:
    server_socket.listen()
    client, addr = server_socket.accept()
    print(f" New connection from {addr}")
    data = client.recv(1024).decode()

    headers = data.split('\n')
    top_line = headers[0].split()

    method = top_line[0]
    filename = top_line[1].strip('/')
    file = fetchfile.fetchfile(filename)
    print(f" Asked for file: {filename}")
    
    if not file:
        print(" File not found in server ")
        client.sendall("404 : File not found".encode())
    else:
        reponse = file.read()
        client.sendall(f" 200 OK : {reponse}".encode())
        file.close()
        print(f" File sent ")
    client.close()
    

