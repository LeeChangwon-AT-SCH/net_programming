from socket import *
import sys
import myTCPServer

port = 2500
BUFFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])

server = myTCPServer.TCPServer(port)
conn, addr = server.Accept()
print('Connected by', addr)

while True:
    data = conn.recv(BUFFSIZE)
    if not data:
        break
    print("Received message:", data.decode())
    conn.send(data)

conn.close()
