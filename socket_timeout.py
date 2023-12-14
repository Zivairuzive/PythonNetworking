# Program file: socket_timeout.py
# can set default timeout on a socket 

import socket 
from log import log 


def set_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log.info(f"Socket timeout is: {s.gettimeout()}")
    s.settimeout(200)
    log.info(f"New socket timeout is: {s.gettimeout()}")
    

set_timeout()