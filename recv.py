#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444  #0-1024 --you check free udp port netstat -nulp

#creating udp socket 
#           ip type     v4        udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#fitting  ip and port with udp socket 
s.bind((recv_ip,recv_port))

#recv data from sender 
while 4>2:
	data=s.recvfrom(256)
	print("Message from sender" , data[0])
	print("Sender IP + port --socket" , data[0])
	reply=raw_input("type your reply")
	sendto(reply,data[1])

s.close()
