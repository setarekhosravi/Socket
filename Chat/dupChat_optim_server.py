"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Basic implementation of chating communication,  duplex form
    optimized version
"""

import socket

HOST = '127.0.0.1'
PORT = 65440

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        con, add = server.accept()
        data = con.recv(1024)
        print(f"Received message from {add}: {data.decode('utf-8')}")

        message = input("Enter your message: ")
        con.sendall(message.encode())