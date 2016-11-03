import socket
def tp_client():
	target_host = "www.baidu.com"
	target_port = 80

	client = socekt.socket(socket.AF_INET,socket.SOCK_STREAM)

	client.connect((target_host,target.port))

	client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

	response = client.recv(4096)
	print response
