import socket, sys, argparse

server = input("Please enter server IP [default = 192.168.4.3]: ")
server = server or "192.168.4.3"



def echo_client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (server, port)
	print("Connecting to %s port %s" % server_address)
	sock.connect(server_address)

	try:
		message = "Test message. This will be echoed"
		print("Sending %s" % message)
		sock.sendall(message.encode("ascii"))
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print("Received: %s" % data.decode("ascii"))
	except socket.error:
		print("Socket error")
	except Exception:
		print("Other exception")
	finally:
		print("Closing connection to the server")
		sock.close()



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Socket Server Example")
	parser.add_argument('--port', action="store", dest="port", type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)