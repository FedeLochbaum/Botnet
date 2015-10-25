from Server import ServerInput, ServerOutput
from Functions import setMessage
from ShellInterface import AppNew

ServerInput("192.168.1.106", 10000).start()
setMessage("None")
ServerOutput("192.168.1.106", 10001).start()

app = AppNew()
app.root.mainloop()
