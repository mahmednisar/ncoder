#!/usr/bin/python3
import os
import crypt
usrname=input("Enter your Username : ")
flag=0
num=[0,1,2,3,4,5,6,7,8,9]
for i in usrname:
	if i in str(num):
		flag=1
if(flag==1):
	print("Invalid User Name")
else:
	pwd="hello"+usrname
	encpwd = crypt.crypt(pwd,"22") #Encrypting Password
	os.system("useradd -p " + encpwd +" "+usrname)
	print("User Added!")

