"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Mini-Projects:
        2- CMD
"""

import socket

server_address = ('127.0.0.1', 65098)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(server_address)
    server.listen()

    con, client_add = server.accept()

    while True:
        command = input("Enter command to execute: ")
        con.sendall(command.encode())
        output = con.recv(1024)
        print(output.decode('utf-8'))