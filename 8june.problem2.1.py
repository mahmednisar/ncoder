#!/usr/bin/python3

import time         #importing time function for time functions
from googlesearch import search     #importing search from googlesearch library
web=input("please Enter some topic: ")               #taking input from user 

url=[]          #declaring blank list 
for i in search(web,stop=10):              #for iteration for searching recursively 
    print(i)                                #printing searched web address
    time.sleep(2)                           #for taking some time for printing we use time sleep function 
    url.append(i)                           #appending web address in the list url
    
print(url)             #print the list

