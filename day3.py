#!/usr/bin/python3
#  now importing  time library 
import  webbrowser 
import  time
import  subprocess
from googlesearch import search
import os
option='''
Press  1  to  start  your  vlc  media player :
Press  2  to  play your fav song in youtube :  
Press  3  to  search something  on google   :  
Press  4  to send telegram message to your fav number  :  
Press  5  to  check current  time and date  :
press  6  to reboot your machine  : 
'''
print(option)

#  taking  input from  user  
#  1 st
choice=input()
#  input function will take input in str  format 
#   conditional  state
if   choice  ==   '5' :
    #   to connect  our BIOS  time 
    current_time=time.ctime()
    print(current_time)

elif  choice  ==  '1'  :
    #   to connect  os level application we use subprocess 
    subprocess.getoutput('vlc')
elif choice == '6':
    com='reboot'
    os.system(com)

elif  choice  ==  '3' :
    data=input("type your search :--->  ")
    webbrowser.open_new_tab('https://www.google.com/search?q='+data)
elif choice == '2':
    data = input("type your song name :---->")
    for i in search(data,stop=1):
        webbrowser.open_new_tab(i)
else  :
    print("hiiii")


