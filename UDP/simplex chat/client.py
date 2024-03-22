"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Basic implementation of UDP server
"""

import socket

IP = '127.0.0.1'
PORT = 7000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    while True:
        message = input("Enter your message: ")
        client.sendto(message.encode(), (IP, PORT))