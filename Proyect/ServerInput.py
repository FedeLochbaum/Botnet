from Server import ServerInput

serv = ServerInput("localhost", 10000)
serv.setMessage("dir")
serv.run()