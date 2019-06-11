#!/usr/bin/python3
#  0.00 - 12.00 ----> Good Morning
#  12.00 - 17.00 ---> Good Afternoon
#  17.00 - 21.00 ---> Good Evening
#  21.00 - 0.00 ----> Good Night
import datetime

name =input("Enter your Name : ")
d=datetime.datetime.now()
curhr=d.hour

if curhr<12:
	print("Good Morning",name+"!")
elif curhr>11 and curhr<=16:
	print("Good Afternoon",name+"!")
elif curhr > 16 and curhr <=21:
	print("Good Evening",name+"!")
else:
	print("Good Night", name+"!")
