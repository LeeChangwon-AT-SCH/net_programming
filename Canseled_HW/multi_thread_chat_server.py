from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024

clients = []

def sendTask(conn):
    while True:
        data = conn.recv(BUFFSIZE)
        print(data.decode())
        if 'quit' in data.decode():
            print(addr, 'exited')
            clients.remove(conn)
            break

        print(time.asctime() + str(addr) + ':' + data.decode())

        for client in clients:
            if client != conn:
                client.send(data)
    conn.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, addr = sock.accept()

    if conn not in clients:
        print('new client', addr)
        clients.append(conn)
        
    th = threading.Thread(target=sendTask, args=(conn,))
    th.start()
