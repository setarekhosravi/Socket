"""
Socket Programming
@author: STRH
Created on 21 March, 2024
    Basic implementation of server
"""

import socket

HOST = '127.0.0.1'
PORT = 12350

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}...")

    con, add = server.accept()
    with con:
        print(f"Connected by {add}")
        data = con.recv(1024)
        print("Received message from client: ", data.decode('utf-8'))
        con.sendall(b"Hello Client!!!")