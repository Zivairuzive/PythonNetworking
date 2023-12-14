#program file: network_service.py
''' Gets  the network service name if you know the port
assuming tcp is used
'''

import socket 
import logging 
from log import log 


def network_service():
    proto_name = "tcp"
    ports = [80, 25, 443]
    for port in ports:
        log.info(f"Port: {port} => Service: {socket.getservbyport(port, proto_name)}")
 
network_service()