import socket, sys, select
from chat_select import send, receive


class ChatClient(object):
    '''command line chat client using select '''
    SERVER_HOST = "127.0.0.1"
    
    def  __init__(self, name, port):
        self.name = name 
        self.port = port 
        self.host = self.SERVER_HOST 
        self.connected = False 
        # Initial prompt 
        self.host_name = socket.gethostname().split(".")[0]
        self.prompt = f'[{'@ '.join((name, self.host_name))}]'
        try:
            #connect to server 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host,port))
            #now connected! 
            print(f"Now connected to chat server @ port: {self.port}")
            self.connected = True 
            #send name to server 
            send(self.sock, f"NAME: {self.name}")
            data = receive(self.sock)
            #contains client address , set it 
            addr = data.split('CLIENT: ')[1]
            self.prompt = f"[{'@'.join((self.name, addr))}]"
        except socket.error as e:
            print("Failed to connect to chat server: ", self.port)
            sys.exit(1)
            
    def run(self):
        ''' Chat client main loop '''
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # wait for input from stdin and socket 
                readable , writeable, exceptional = select.select([self.sock, self.sock],[],[])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif sock == self.sock:
                        try:
                            data = receive(self.sock)
                        except socket.error as data:
                            print(f"Client Shutting down: {e}")
                            self.connected =False 
                            break 
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print("Client interrupted")
                self.sock.close()
                break
 
if __name__ == '__main__':
    ChatClient('HP', 8080).run()