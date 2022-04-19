import socket
import struct
import sys

class dnsClient:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        # DNS Query Header
        self.TransactionId = 1
        self.Flag = 0x0100
        self.Questions = 1
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0
    # Processing DNS rsp
    def response(self, packet):
        dnsHeader = packet[:12]
        dnsData = packet[12:].split(b'\x00', 1)

        ansRR = packet[12 + len(dnsData[0]) + 5:12 + len(dnsData[0]) + 21]
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domain_name, ip_addr)
        
    # Create DNS query
    def query(self):
        # DNS header packing
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query = query + struct.pack('!HH', self.Questions, self.AnswerRRs)
        query = query + struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        part = self.domain_name.split('.')

        for i in range(len(part)):
            query = query + struct.pack('!B', len(part[i]))
            query = query + part[i].encode()

        query = query + b'\x00'

        query_type = 1  # Type  : A
        query_class = 1 # Class : IN
        query = query + struct.pack('!HH', query_type, query_class)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ('220.69.193.130', 53)
        sock.sendto(query, addr)
        packet, address = sock.recvfrom(65535)
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = dnsClient(sys.argv[1])
        client.query()

