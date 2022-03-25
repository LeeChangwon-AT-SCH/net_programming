import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
sock.send(b'Changwon Lee')
b_id = sock.recv(4)
student_id = int.from_bytes(b_id, 'big')
print(student_id)
sock.close()