import socket 
from log import log 
import ntplib
from time import ctime 



def server_time():
    # create a ntp client
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request("pool.ntp.org")
    log.info(ctime(response.tx_time))
    
    
    
server_time()