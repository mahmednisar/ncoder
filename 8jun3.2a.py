#!/usr/bin/Python3
import webbrowser
from googlesearch import search

f=open("urls.txt","w")
topic = input("Enter topic to search : ")
url=search(topic,stop=10)
for i in url:
	f.write(i+"\n")
webbrowser.open("https://www.google.com/search?q="+topic)
