import socket
import random
def recv_file(client: socket.socket):
    data =
    client.send("".encode())



def create_file(filename: str, client: socket.socket):
    try:
        file_open = open(f"{default_filepath}{filename}.7z", "x")
    except FileExistsError:


default_filepath = "C:/Backup/"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0,0,0,0', 5000))
clients = []
while True:
    server_socket.listen()
    clients.append(server_socket.accept())


