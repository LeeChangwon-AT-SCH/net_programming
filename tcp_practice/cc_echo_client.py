from re import T
import socket

BUFFSIZE = 1024

s = socket.create_connection(('localhost', 2500))

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFFSIZE)
    if not data:
        break
    print("Received message: %s" % data.decode())

s.close