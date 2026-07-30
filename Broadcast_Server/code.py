import socket
import argparse

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',required= True)
parser.add_argument('-a','--address', required=True)

args = parser.parse_args()

server_ip = args.address
server_port = int(args.port)


server.bind((server_ip,server_port))
server.listen()

print(f"Server listening on {server_ip}:{server_port}")

connections = [] 

def broadcast(data):
    dead = []
    for conn, addr in connections:
        try:
            conn.sendall(data)
        except OSError:
            dead.append((conn, addr))
    for d in dead:
        connections.remove(d)

while True:
    conn, addr = server.accept()
    connections.append((conn, addr))
    print(f"New connection: {addr} | total: {len(connections)}")
    broadcast(b"a new client joined\n")  
