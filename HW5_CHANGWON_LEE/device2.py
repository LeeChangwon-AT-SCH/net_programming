from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1522))
s.listen(5)
print('Please wating..')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        data = data.decode()
        print(data)
        if data == 'Request':
            heartbeat = str(random.randrange(40, 141))
            steps = str(random.randrange(2000, 6001))
            cal = str(random.randrange(1000, 4001))
            total = heartbeat + ' ' + steps + ' ' + cal
            print(total)
            client.send(total.encode())
        elif data == 'quit':
            break
    if data == 'quit':
        break

    client.close()