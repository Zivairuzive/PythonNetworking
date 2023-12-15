# Program file : sock_blocking.py
# 


import socket 
from log import log 


def sock_modes():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    s.setblocking(1)
    s.bind(("127.0.0.1", 8000))
    sock_address = s.getsockname()
    log.info(f"Trivial socket launched on : {str(sock_address)}")
    
    while(True):
        s.listen(1)
        conn, addr = s.accept()
        print(conn)
        
sock_modes()