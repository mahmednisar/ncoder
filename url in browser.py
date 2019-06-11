#!/usr/bin/python3

#Store top 5 url in a list and then open those url in browser

#importing time function for time functions
import time 
#importing webbrowser library
import  webbrowser       
#importing search from googlesearch library
from googlesearch import search  

#taking input from user  
web=input("please Enter some topic: ")              
#declaring blank list to store result.
url=[]          
#for iteration for searching recursively 
for i in search(web,stop=5):          
     #printing searched web address
    print(i)
	#searching extracted address into a new tab in browser
    webbrowser.open_new_tab(i)    
	#for taking some time for printing we use time sleep function                        
    time.sleep(2)                           	
	#appending web address in the list url
    url.append(i)                           
    	#print the list

print(url)
