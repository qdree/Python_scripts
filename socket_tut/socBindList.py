import socket
import sys
from _thread import *

host = ''
port = 5554
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host, port))
except socket.error as e:
	print (str(e))

s.listen(5)



def threaded_client(conn):
	conn.send(str.encode('Welcome type your info\n'))

	while True:
		data = conn.recv(2048)
		reply = data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode('Server output: ' + reply))
		print (reply)

		if reply == "Bye":
			print ("It was the last message, client decided to stop communication")
			return
	conn.close()

while True:

	conn, addr = s.accept()
	print ('connected to: ' + addr[0] + ':' + str(addr[1]))
	start_new_thread(threaded_client, (conn, ))
	