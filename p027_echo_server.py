import socket, sys, argparse

server = input("Please enter server IP [default = 192.168.4.3]: ")
server = server or "192.168.4.3"
data_payload = input("Please enter data payload [default = 2048]: ")
data_payload = data_payload or "2048"
data_payload = int(data_payload)
backlog = 5

def echo_server(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = (server, port)
	print("Starting up echo server on %s port %s" % server_address)
	sock.bind(server_address)
	sock.listen(backlog)
	while True:
		print("Waiting to receive message from client")
		client, address = sock.accept()
		data = client.recv(data_payload)
		if data:
			print("Data: %s" % data.decode("ascii"))
			client.send(data)
			print("sent %s bytes back to %s" % (str(len(data)), address))
		client.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Socket Server Example")
	parser.add_argument("--port", action="store", dest="port", type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)