from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2017))
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
            temp = str(random.randrange(0, 41))
            illum = str(random.randrange(0, 101))
            humid = str(random.randrange(70, 151))
            total = temp + ' ' + humid + ' ' + illum
            print(total)
            client.send(total.encode())
        elif data == 'quit':
            break
    if data == 'quit':
        break

    client.close()