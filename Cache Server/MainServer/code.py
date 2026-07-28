import socket
import argparse
import fetchfile

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--port',required=True)
parser.add_argument('-a', '--address', required= True)

args = parser.parse_args()

main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

main_server.bind((args.address, int(args.port)))
print(f" Socket created at {args.address} : {args.port}")
while True:
    main_server.listen()
    client, addr = main_server.accept()
    print(f" New connection from {addr}")
    filename = client.recv(1024).decode()

    file = fetchfile.fetchfile(filename)

    print(f" Asked for file: {filename}")
    
    if not file:
        print(" File not Found")
        client.sendall("404: File not found".encode())
        client.close()
        continue
        
    else:
        reponse = file.read()
        client.sendall(f" 200 OK : {reponse}".encode())
        file.close()
        print(f" File sent ")
    client.close()