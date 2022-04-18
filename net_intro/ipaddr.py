import ipaddress # python ip addr 표현 및 처리 모듈
 
addr4 = ipaddress.ip_address('192.168.0.1')
print(addr4)

addr6 = ipaddress.ip_address('2001:A8::1')
print(addr6)

print(addr4.version)
print(addr6.version)

net = ipaddress.ip_network('114.71.220.0/24')
print(net)
print(net.with_netmask)
print(net.num_addresses)
print(net.netmask)
print(net.hostmask)
