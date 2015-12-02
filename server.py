import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8360))
serversocket.listen(5)

while 1:
	print("1")
	(clientsocket, address) = serversocket.accept()
	print("2")
	print(address)
	print(clientsocket)
serversocket.close()