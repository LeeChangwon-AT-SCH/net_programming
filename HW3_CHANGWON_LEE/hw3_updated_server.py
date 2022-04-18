from socket import *
import math
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('Please wating..')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        # parsing
        data = data.decode()
        # 공백처리 (anywhere)
        parsing_data = data.replace(' ', '')
        print(parsing_data)
        if '+' in data:
            parsing_data = parsing_data.split('+')
            print(parsing_data)
            result = int(parsing_data[0]) + int(parsing_data[1])
        if '-' in data:
            parsing_data = parsing_data.split('-')
            result = int(parsing_data[0]) - int(parsing_data[1])
        if '*' in data:
            parsing_data = parsing_data.split('*')
            result = int(parsing_data[0]) * int(parsing_data[1])
        if '/' in data:
            parsing_data = parsing_data.split('/')
            result = int(parsing_data[0]) / int(parsing_data[1])
            result = round(result, 1)

        result = str(result)
        client.send(result.encode())
    
    client.close()