import socket
from Functions import setMessage, getMessage, addConnection
import threading
#from _dbus_bindings import Message

class Server(threading.Thread):
    
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port        

    def run(self):
        
        print(str(self.ip) + " " + str(self.port))
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        # Bind the socket to the port
        server_address = (self.ip, self.port)
        sock.bind(server_address)        
        # Listen for incoming connections
        sock.listen(1000)        
        while True:
            # Wait for a connection
            connection, client_address = sock.accept()            
            try:
                addConnection(client_address,connection)
                self.runSpecific(connection)                              
            finally:
                # Clean up the connection
                connection.close()

class ServerOutput(Server):

    def init(self):
        self.ip = "10.12.5.43"
        self.port = 10001
            
    def runSpecific(self, connection):
        data = connection.recv(160000).decode("utf-8")
        print(data)
    
class ServerInput(Server):
    
    def init(self):
        self.ip = "10.12.5.43"
        self.port = 10000

    def conectWithOneConnection(self,key,command):
        connection = self.connections.get(key) 
        setMessage(command)
        self.runSpecific(connection)
    
    def runSpecific(self, connection):
        print(getMessage())
        connection.sendall(getMessage())


