"""
Socket Programming
@author: STRH
Created on 21 March, 2024
    Basic implementation of chating communication,  duplex form
"""

import socket
import threading

HOST = '127.0.0.1'
PORT = 65400

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connected to the server.")

    while True:
        message = input("Enter your message: ")
        client.sendall(message.encode())
        data = client.recv(1024)
        print(f"Received message from the server: {data.decode('utf-8')}")