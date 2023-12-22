import socket
import select 
import sys
import pickle
import signal 
import argparse 
import struct 

SERVER_HOST = "127.0.0.1"
CHAT_SERVER = 'server'

#utilities 
def send(ch, *args):
    buf = pickle.dumps(args)
    val = socket.htonl(len(buf))
    size = struct.pack("L",val)
    ch.send(size)
    ch.send(buf)
    
    pass 

def receive(chann):
    ...

class ChatServer(object):
    
    def __init__(self, port, backlog=5):
        self.clients = 0 
        self.client_map = {}
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((SERVER_HOST, port))
        print(f"Server listening on {port}")
        self.server.listen(backlog)
        #catch keyboard interrupts

        # breakpoint()
        signal.signal(signal.SIG_IGN, self.signal_handler)
    
    def signal_handler(self, sign_num, frame):
        '''clean client outputs'''
        # close the server 
        print("Shutting down server")
        for output in self.outputs:
            output.close()
        self.server.close()
        
    def get_client_name(self, client):
        client = self.client_name[client]
        host, name = info[0][0], info[1]
        return '@'.join((host, name))
    
    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        
        running = 1
        while running:
            try:
                readable,writable, exceptional = select.select(inputs, self.outputs, [])
            except select.error as e:
                break 
            for sock in readable:
                if sock == self.server:
                    #handle server socket 
                    client, address = sock.accept()
                    print(f"Chat server: got connection {client.fileno} from  {address}")
                    #read the login name 
                    cname = receive(client).split("NAME: ")[1]
                    
                    #compute client name and send back 
                    self.clients +=1
                    send(client, F'CLIENT: {str(address[0])}')
                    inputs.append(client)
                    self.client_map[client] = (address, cname)
                    #send joining information to other clients 
                    msg = f'\n Connected: New client {self.clients} from {self.get_client_name(client)}'
                    for output in self.outputs:
                        send(msg)
                        
                    self.outputs.append(client)
                elif sock == sys.stdin:
                    # handle standard input 
                    junk = sys.stdin.realine()
                    running = False
                else:
                    #handle all other sockets 
                    try:
                        data = receive(sock)
                        if data:
                            #Send as new client's message
                            msg = f'\n#[{ self.get_client_name(sock)}] >>{data}'
                            #send data to all except yourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                                
                        else:
                            print(f"Chat server: {sock.fileno} hang up")
                            self.clients -=1
                            sock.close()
                            self.outputs.remove(sock)
                            
                            #Sending client leaving to others 
                            msg = f'\n Left the room: Client from {self.get_client_name(sock)}'
                            for output in self.outputs:
                                send(msg, output)
                    except socket.error as e:
                        #remove 
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()

f = ChatServer(8080)
# f.run()