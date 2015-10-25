import threading 
from _socket import socket
message = ""
connections = dict()

mutex = threading.Lock()

def setMessage(mes):
    global message
    with mutex:
        print("SET - Global ->" + mes)
        message = mes
        return  #+ " @ " + str(isFinish)
    
def getSocket():
    return connections.keys()
        
def getMessage():
    with mutex:
        print("Global ->" + message)        
        return bytes(message, "utf-8")
    
def addConnection(sock, connection):
    global connections
    connections[sock] = connection
    return
    
def getConnections():
    return connections