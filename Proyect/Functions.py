import threading 
message = ""
connections = dict()

mutex = threading.Lock()

def setMessage(mes):
    global message
    with mutex:
        print("SET - Global ->" + mes)
        message = mes
        return  #+ " @ " + str(isFinish)
    
def getIps():
    return connections.keys()
        
def getMessage():
    with mutex:
        print("Global ->" + message)        
        return bytes(message, "utf-8")
    
def addConnection(ip_user, connection):
    global connections
    connections[ip_user] = connection
    return
    
def getConnections():
    return connections