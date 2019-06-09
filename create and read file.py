
#!/usr/bin/python3

#read and write both using w+
f=open('hello1.txt','r+')  #this will read a file first
f.write("linux")
print(f.read)
f.close()

f.seek(1)   #move the cursor 
print(f.read())

#read and write both using w+
f=open('hello1.txt','w+')  #this will create a file first
f.write("hhhhhhhhiiiiiiiiiiii")
f.write("\n")
f.write("ok")
f.seek(1)   #move the cursor 
print(f.read())
f.close()
