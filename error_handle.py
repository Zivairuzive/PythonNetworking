#Program file : error_handle.py 
#Handles socket errors gracefully 

import socket 
from log import log 
import argparse, sys 

def handle():
    #setup agrparse 
    parser = argparse.ArgumentParser(description="Socket error example")
    parser.add_argument("--host", action="store", dest="host", required= False)
    parser.add_argument("--port", action="store", dest="port", type=int, required= False)
    parser.add_argument("--file", action="store", dest="file", required= False)
    
    args_given = parser.parse_args()
    host, port, filename = args_given.host, args_given.port , args_given.file
    # try to create a socket 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        log.warning(f"Failed to create socket: {e}")
        sys.exit(1)
    
    try:
        s.connect((host, port))
    except socket.error as e:
        log.warning(f"Failed to connect: {e}")
        sys.exit(1)
    # try sending the data 
    try:
        msg = f"GET {filename}"
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        log.warning(f"Could not send data: {e}")
        sys.exit(1)
    while 1:
        # block - waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            log.warning(f"Failed to receive data {e}")
            sys.exit(1)
        
        if not len(buf):
            break 
        #write rhe received data 
        sys.stdout.write(buf.decode('utf-8'))
  
handle()