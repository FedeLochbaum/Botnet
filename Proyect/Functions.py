import threading 
from tkinter.constants import END

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
    
def addConnection(clientIp):
    global connections
    if not clientIp in connections.keys():
        updateListIp(clientIp)       
    connections[clientIp] = ""
    
def getConnections():
    return connections

appNew = None

def getApp():
    return appNew

def setApp(appnew):
    global appNew
    appNew = appnew
    
def updateListIp(value):
    getApp().listIps.insert(END, value)