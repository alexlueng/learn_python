import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)


try:
	message = b'This is a message. It will be repeated'
	print('sending %s' % message)
	sock.sendall(message)
	amount_received = 0
	amount_excepted = len(message)
	while amount_received < amount_excepted:
		data = sock.recv(16)
		amount_received += len(data)
		print('receiving "%s"' % data)

finally:
	print(sys.stderr, 'closing socket')
	sock.shutdown(2)
	sock.close()