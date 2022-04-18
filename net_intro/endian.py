import socket 

temp = 1234

print(hex(temp))
temp2 = socket.htons(temp)
print(hex(temp2))
print(hex(socket.ntohs(temp2)))