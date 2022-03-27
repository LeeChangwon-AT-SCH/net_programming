from socket import *

s = socket()
s.bind (('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    req = req[0].split(' ')
    # print(req)
    req = req[1].split('/')
    # print(req)
    req = req[1]
    print(req)

    if req == 'index.html':
        print(req)
        f = open("index.html", 'r', encoding='utf-8')
        mimetype = 'text/html' 
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read()
        c.send(data.encode('euc-kr'))
    elif req == 'iot.png':
        f = open('iot.png', 'rb')
        mimetype = 'image/png'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read()
        c.send(data)
    elif req == 'favicon.ico':
        f = open('favicon.ico', 'rb')
        mimetype = 'image/x-icon'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        c.send(b'\r\n') 
        data = f.read()
        c.send(data)
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
    c.close()
