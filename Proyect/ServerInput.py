from Server import ServerInput, ServerOutput
from Functions import setMessage
from time import sleep
from ShellInterface import AppNew

ServerInput("192.168.1.105", 10000).start()
setMessage("None")
ServerOutput("192.168.1.105", 10001).start()

app = AppNew()
app.root.mainloop()
