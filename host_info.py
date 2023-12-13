import socket 

def host_name():
    host__name = socket.gethostname()
    host_ip = socket.gethostbyname(host__name)
    print(f"Machine name : {host__name} with IP : {host_ip}")
    return 

if __name__ == "__main__":
    host_name() 