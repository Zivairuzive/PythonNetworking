# Program file : socket_buffer
# program can edit the socket buffer 

import socket 
from log import log

SEND_BUFF_SIZE = RECV_BUFF_SIZE = 4096


def socket_buffer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #get socket send buffer size
    buf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    log.warning(f"Buffer size [Before] is {buf}")
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    new_buf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    log.warning(f"New buffer size [After] is {new_buf}")
    


socket_buffer()