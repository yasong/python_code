import socekt

def udp_client():
	target_host = "127.0.0.21"
	target_port = 80
	
	client = socket.socket(socekt.AF_INET, socket.SOCK_DGRAM)
	
	client.sendto("AAABBBCCC", (target_host,target_port))
	
	data, addr = client.recvfrom(4096)
	
	print data
