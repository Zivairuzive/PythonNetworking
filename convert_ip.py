#converting ip to binary formats

import socket
from binascii import hexlify



def convert_ip():
    sample_addresses = ['127.168.0.1', socket.gethostbyname(socket.gethostname())]
    for addr in sample_addresses:
        #returns 32bit packed binary format 
        packed_ip = socket.inet_aton(addr)
        unpacked = socket.inet_ntoa(packed_ip)
        
        print(f"IP Address {addr}: Packed {hexlify(packed_ip)}")
        print(f"IP Address {addr}: Unpacked {unpacked}")

if __name__ =="__main__":
    convert_ip()
    