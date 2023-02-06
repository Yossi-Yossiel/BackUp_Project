import socket
import random
import sys
import time
import mysql.connector


def establish_connection(client: socket.socket):
    rand = random.randint(100, 999)
    client.send(f"{rand}".encode())
    data = client.recv(1024).decode()
    dataArr = data.split(" ")
    client.send(f"{dataArr[0]} {int(dataArr[1])+1}".encode())
    data = client.recv(1024)
    if data == "ok":
        client.send(b'Please provide the file name and file size')
        file_name = client.recv(1024).decode()
        file_size = int(client.recv(1024).decode())
    else:
        client.send("connection not stable. disconnecting".encode())
        client.close()


def recv_file(client: socket.socket, file_name: str, file_size: int):
    data = client.recv(1024)
    client.send("".encode())


def create_file(filename: str, client: socket.socket):
    try:
        file_open = open(f"{default_filepath}{filename}.7z", "w")
    except Exception as e:
        print(e)
        sys.exit()


default_filepath = "C:/Backup/"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
clients = []
while True:
    server_socket.listen()
    clients.append(server_socket.accept())

