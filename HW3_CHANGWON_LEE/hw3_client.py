from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Enter the calculation formula.\n')
    if msg == 'q':
        break
    s.send(msg.encode())

    print('Answer: ', s.recv(1024).decode())

s.close()