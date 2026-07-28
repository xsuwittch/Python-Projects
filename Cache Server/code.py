import socket
import argparse
from urllib import request, error
import fetchfile
parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',required=True)
parser.add_argument('-a','--address',required=True)


serverip = '127.0.0.1'
serverport= 9000
args = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Main_server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
        Main_server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        Main_server_soc.connect((serverip , serverport))
        Main_server_soc.sendall(filename.encode())
        response = b""
        while True:
            chunk = Main_server_soc.recv(4096)
            if not chunk:
                break
            response += chunk
        
        client.sendall(f" 200 OK : {response}".encode())
        print(" File sent from main server ")

    else:
        reponse = file.read()
        client.sendall(f" 200 OK : {reponse}".encode())
        file.close()
        print(f" File sent ")
    client.close()
    
    

