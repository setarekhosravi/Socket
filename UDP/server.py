"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Basic implementation of UDP server
"""

import socket

IP = '127.0.0.1'
PORT = 7000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((IP, PORT))
    print(f"Server is listening on {IP}:{PORT}")

    data, add = server.recvfrom(1024)
    print(f"Recieved message from client: {data.decode('utf-8')}")

    message = input("Enter your message: ")
    server.sendto(message.encode(), add)

    server.close()