from Server import ServerInput

serv = ServerInput("localhost", 10000)
serv.attackDdos("localhost",2, 1)
serv.run()
