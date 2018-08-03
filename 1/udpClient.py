import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Micheal, b'Tracy, b'Sarah]:
	s.send(data, (172.0.0.1, 9999))
	print(s.recv(1024).decode('utf-8'))
s.close()

