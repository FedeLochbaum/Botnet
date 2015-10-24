from Server import ServerInput, ServerOutput
from Functions import setMessage
from time import sleep

ServerInput().start()
setMessage("None")
ServerOutput().start()

sleep(10)

setMessage("dir @ False")

sleep(10)

setMessage("dir @ True")
