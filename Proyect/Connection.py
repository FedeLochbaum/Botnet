import os
class Connection:

    def __init__(self,socket,name):
        self.socket = socket
        self.name = name
        
        
    def getSocket(self):
        return self.socket
    
    def getName(self):
        return self.name