# program file: remote_host_ip
import socket 

import sys 

def get_remote_ip():
    address = sys.argv[1]
    try:
        remote_host = f"IP of {address} is {socket.gethostbyname(address)}"
        print(remote_host)
    except socket.error as msg:
        remote_host = f"{address}:{msg}"
        print(remote_host)
    return 



if __name__ == "__main__":
    get_remote_ip()
    