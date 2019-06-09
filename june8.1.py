#!/usr/bin/python3

import sys

#another method to take  input from user
x=sys.argv[1:]
print(sys.argv[1:])

sum=0
for i in x:
    print("hii")
    sum=sum+int(i)
    
print(sum)
