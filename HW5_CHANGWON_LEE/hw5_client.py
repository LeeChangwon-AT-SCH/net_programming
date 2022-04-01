from socket import *
from tkinter.ttk import setup_master
import time

s_dev1 = socket(AF_INET, SOCK_STREAM)
s_dev2 = socket(AF_INET, SOCK_STREAM)
s_dev1.connect(('localhost', 2017))
s_dev2.connect(('localhost', 1522))

f = open('.\HW5_CHANGWON_LEE\data.txt', 'a')

while True:
    msg = input('Enter the device from which you want to get the data.\n')
    if msg == 'quit':
        s_dev1.send('quit'.encode())
        s_dev2.send('quit'.encode())
        break
    elif msg == '1':
        s_dev1.send('Request'.encode())
        rsp = s_dev1.recv(1024).decode()
        data = rsp.split(' ')
        temp = data[0]
        humid = data[1]
        illum = data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device1:' + ' ' + 'Temp=' + temp + ', Humid=' + humid + ', Illum=' + illum + '\n'
        print(line)
        f.write(line)
    elif msg == '2':
        s_dev2.send('Request'.encode())
        rsp  = s_dev2.recv(1024).decode()
        data = rsp.split(' ')
        heartbeat = data[0] 
        steps = data[1]
        cal = data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device2:' + ' ' + 'Heartbeat=' + heartbeat + ', Steps=' + steps + ', Cal=' + cal + '\n'
        print(line)
        f.write(line)
    # print('Get data: ', rsp)

s_dev1.close()
s_dev2.close()
f.close()