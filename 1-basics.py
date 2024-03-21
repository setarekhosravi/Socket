import socket

IP = '127.0.0.1'
PORT = 3995
# ping 127.0.0.1 in terminal

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # choose IPv4 as AF_INET
    server.bind((IP, PORT))                                       # choose TCP as SOCK_STREAM
    server.listen()
    print("server listening to incoming connections!")

    con, add = server.accept()