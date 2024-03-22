"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Mini-Projects:
        2- CMD
"""

import socket
import subprocess

server_address = ('127.0.0.1', 65098)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(server_address)

    while True:
        command = client.recv(1024).decode('utf-8')
        process = subprocess.Popen(command, stdout= subprocess.PIPE, stderr= subprocess.PIPE, shell= True)
        output, error = process.communicate()

        if error:
            client.sendall(error)
        else:
            client.sendall(output)