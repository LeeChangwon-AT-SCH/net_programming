import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9000)) # 소켓과 종단점 결합 # PC내 모든 IP주소가 바인딩
sock.listen(5)        # 클라이언트 연결 대기

# client: 연결된 클라이언트와 실제 통신을 수행하는 소켓
# addr: 연결된 클라이언트의 IP addr and port number
# TCP Server 
while True:
    client, addr = sock.accept() # 클라이언트 연결 수용
    client.send(b'Hello ' + addr[0].encode())
    data = client.recv(1024)
    print(data)
    client.close()