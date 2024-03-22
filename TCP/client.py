"""
Socket Programming
@author: STRH
Created on 21 March, 2024
    Basic implementation of client
"""

import socket

HOST = '127.0.0.1'  # IP of server
PORT = 12350

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b"Hello Server!")
    data = client.recv(1024)

print("Received message from Server: ", data.decode("utf-8"))