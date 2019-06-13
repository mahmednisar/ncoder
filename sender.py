#!/usr/bin/python2

import socket

recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>2:
	msg=raw_input("enter your message here: ")
	s.sendto(msg,(recv_ip,recv_port))

	#recv data from reciever
	print(s.recvfrom(10))



s.close()
