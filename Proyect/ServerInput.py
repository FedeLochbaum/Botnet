from Server import ServerInput, ServerOutput
from Functions import setMessage
from ServerInterface import AppNew

ServerInput("192.168.0.108", 10000).start()
setMessage("None")
ServerOutput("192.168.0.108", 10001).start()


app = AppNew()
app.root.mainloop()
