# program file: remote_host_ip
# ip lookup

import socket 
import logging 
import sys

log = logging.getLogger("Remote Host:")
logging.basicConfig(level=logging.DEBUG)

def get_remote_ip():
    if len(sys.argv) >=2:
        address = sys.argv[1:]
        for addr in address:
            try:
                remote_host = f" IP of {addr} is {socket.gethostbyname(addr)}"
                log.info(remote_host)
            except socket.error as msg:
                remote_host = f"{addr}:{msg}"
                log.warning(remote_host) 
    else:
        log.warning("Provide host address as command line argument")
        



if __name__ == "__main__":
    get_remote_ip()
    