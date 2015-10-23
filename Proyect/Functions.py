import threading 
message = ""

mutex = threading.Lock()

def setMessage(mes, isFinish):
    global message
    with mutex:
        message = mes+ " @ " + str(isFinish)
        
def getMessage():
    global message
    with mutex:        
        return bytes(message)
    