# Program file :: echo client 
# Create a async client 

import socketserver 
import os
import threading, socket 

SERVER_HOST ='127.0.0.1'
BUF_SIZE = 1024
# I ran the server on this port 
# client has to know server address and port inorder to connect 
# replace with server address
PORT = 64994 
#Message to send to server 
MESSAGE = "Hello Echo Server"

class FockedClient(object):
    '''Client to test a focking server'''
    def __init__(self, host, port, name=None):
        if name:
            self.client_name = name
        #create a socket 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = s
        #connect to server 
        self.sock.connect((host, port))
        
    def run(self):
        '''Client sending data to server'''
        c_process = os.getpid()
        print(F"PID {c_process} send echo message to the server: {MESSAGE}")
        data = bytes(MESSAGE, "utf-8")
        sent_data = self.sock.send(data)
        print(f"Client {self.client_name} has sent: {sent_data} characters")
        #Display received data
        response = self.sock.recv(BUF_SIZE)
        print(f"PID: {c_process} received {response[5:]}")
    
    def cleanup(self):
        '''Clean up the socket client'''
        self.sock.close()
        
        

if __name__ == "__main__":
    #Launch 1000 clients
    import time 
    c_start = time.time() 
    for i in range(1, 10):
        client_name = f'client_{i}'
        client = FockedClient(SERVER_HOST, PORT, name=client_name)
        print(f"Running {client_name}")
        client.run()
        print(f"Closing socket {client_name}")
        client.cleanup()
    print(f"Finished in {time.time() - c_start} for {i} requests")