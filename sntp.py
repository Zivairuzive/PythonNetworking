import socket 
import struct , sys, time 

NTP_SERVER = "0.uk.pool.ntp.org"
time_ = 2208988800

def get_time():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47*'\0' # ntp protocol data 
    s.sendto(data.encode("utf-8"), (NTP_SERVER, 123))
    data, address = s.recvfrom(1024)
    print(data, kk)
    t = struct.unpack('!12I', data)[10]
    t-= time_
    print(time.ctime(t))
    
    
get_time()