import socket
import argparse

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',required= True)
parser.add_argument('-a','--address', required=True)

args = parser.parse_args()

server_ip = args.address
server_port = int(args.port)


server.bind((server_ip,server_port))

print(f" Server Created at {server_ip}  : {server_port}")



