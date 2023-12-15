#Pogram file: socket reuse 

import socket 
from log import log 

def reuse():
    #create socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Get old socket state 
    old_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    log.info(f"Old state is: {old_state}")
    
    #Enable socket reuse option 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Get new socket state 
    new_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    log.info(f"New state is: {new_state}")
    
    port = 8484
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("", port))
    srv.listen(3)
    log.info(f"Listening on port {port}")
    while True:
        try:
            con,addr = srv.accept()
            # breakpoint()
            log.info(f"Connected by {addr[0]}:{addr[1]}")
            import os 
            d = con.recv(4096)
            #trying to decode received data
            to_py = bytes.decode(d)
            # check what data is received from client
        except KeyboardInterrupt as e:
            break 
        except socket.error as e:
            log.critical(e)
            
    
    
    
reuse()