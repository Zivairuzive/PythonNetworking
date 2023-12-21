import socketserver
import os, threading 


BUF_SIZE = 1024
SERVER_HOST = "127.0.0.1"
PORT = 0

class FockingServerHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        # send the echo back to the client 
        c_process = os.getpid()
        data = str(self.request.recv(BUF_SIZE), 'utf-8')
        response = f'{c_process}: {data}'
        print(f"Server send response [c_process: data] = {response}")
        self.request.send(bytes(response, "utf-8"))
        return 
    

class FockingServer(socketserver.TCPServer, socketserver.ThreadingMixIn):
    '''Everything has been inherited from the parents'''



def start():
    #Launch the server 
    server = FockingServer((SERVER_HOST, PORT), FockingServerHandler)
    #retrieve port number 
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    print(f'To serve on: {ip}: {port}')
    # server.serve_forever()
    #set daemon to true, prevents hanging on exit 
    # server_thread.setDaemon(True)
    server_thread.start()
    print(f"server loop running on: PID {os.getpid()}")
    server_thread.run()
    
    
    
if __name__ == "__main__":
    start()