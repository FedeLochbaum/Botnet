import threading 
message = ""

mutex = threading.Lock()

def setMessage(message, isFinish):
    with mutex:
        message = message+ " @ " + str(isFinish)
        
def getMessage():
    with mutex:
        return message
    