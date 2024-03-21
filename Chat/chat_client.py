"""
Socket Programming
@author: STRH
Created on 21 March, 2024
    Basic implementation of chating communication
"""

import socket

HOST = '127.0.0.1'
PORT = 65450

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        message = input("Enter a message: ")
        client.sendall(message.encode())