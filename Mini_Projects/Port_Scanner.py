"""
Socket Programming
@author: STRH
Created on 22 March, 2024
    Mini-Projects:
        1- Port Scanner
"""

import socket

# Define target IP and Ports
IP = '127.0.0.1'
# IP = input("Enter IP address: ")
Ports = [80, 443, 8000, 53946]

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in Ports:
    try:
        sockt.connect((IP, port))
        print(f"Port {port} is open...")
    except:
        print(f"Port {port} is closed...")

sockt.close()