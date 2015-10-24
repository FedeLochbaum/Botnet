from Server import ServerInput, ServerOutput
from Functions import setMessage
from time import sleep
from ShellInterface import AppNew

ServerInput().start()
setMessage("None")
ServerOutput().start()

app = AppNew()
app.root.mainloop()
