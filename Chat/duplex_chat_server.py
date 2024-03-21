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

def handle_client(conn, add):
    print(f"New client connected: {add}")
    with conn:
        data = conn.recv(1024)
        print(f"Received message from {add}: {data.decode('utf-8')}")
        message = input("Enter your message: ")
        conn.sendall(message.encode())

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server is listening on {HOST}:{PORT}")
        while True:
            conn, add = server.accept()
            threading.Thread(target=handle_client, args=(conn,add)).start()

start_server()