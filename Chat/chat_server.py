"""
Socket Programming
@author: STRH
Created on 21 March, 2024
    Basic implementation of chating communication
"""

import socket

HOST = '127.0.0.1'
PORT = 65450

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Server started...")
    print("Listening for incoming connections...")

    con, add = server.accept()
    print("Client connected: ", add)
    while True:
        data = con.recv(1024)
        print(f"Received {data.decode("utf-8")} from {con.getpeername()}")