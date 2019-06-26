
#The given scenario is to find the events described in the following webpages:
#https://10times.com/top100/technology
#https://blog.bizzabo.com/technology-events
#https://www.nasscom.in/events

#The first two webpage has the data in tabular for which can be found in rows under the tags <tr>
#the last link has the data in the form of blocks

# the contents of the webpage needs to be scrapped for the data and should be defined by a structure.

#EVENT_NAME
#EVENT_COUNTRY
#EVENT_CITY
#EVENT_DATE
#EVENT_TIME
#EVENT_DETAILS
#EVENT_TYPE
#EVENT_FOR

#Show the result as each event which can be sorted by city as well as country.


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
#import spacy
from urllib.request import urlopen
import lxml.html as lh
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  

'''https://10times.com/top100/technology','https://blog.bizzabo.com/technology-events','https://www.nasscom.in/events','''
  
urls=['http://www.psgtech.edu/aisgsc2019/index.html','https://www.eventbrite.com/d/india--bangalore/tech-conferences/']

'''
aggreagate=[
['html', 'head', 'meta', 'link', 'title', 'script', 'body', 'p', 'a', 'header', 'div', 'img', 'ul', 'li', 'form', 'h2', 'label', 
'input', 'span', 'h4', 'select', 'option', 'fieldset', 'legend', 'i', 'strong', 'h1', 'nav', 'button', 'h5', 'h3', 'br'],
['html', 'head', 'meta', 'title', 'link', 'script', 'style', 'body', 'header', 'nav', 'div', 'a', 'img', 'ul', 'li', 'form', 'input',
 'i', 'noscript', 'iframe', 'section', 'h1', 'span', 'small', 'br','select', 'option', 'h2', 'strong', 'table', 'tbody', 'tr', 'th', 'td', 'ins', 'footer', 'hr', 'p', 'u'],
['html', 'head', 'meta', 'title', 'link', 'script', 'style', 'body', 'div', 'span', 'a', 'img', 'i', 'ul', 'li', 'form', 'input', 'h3', 'h1',
'p', 'strong', 'table', 'tbody', 'tr', 'td', 'thead', 'th', 'br', 'h4', 'gcse:searchresults-only', 'noscript', 'iframe']]

aggreagate_list=[]

direct=[]

direct_list=[]
'''
def is_executable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'image' in content_type.lower():
        return False
    if 'pdf' in content_type.lower():
        return False
    if 'application' in content_type.lower():
        return False
    return True


def webpage_type_analyzer(url):
    res=[]
    req=requests.get(url)
    print(req)
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html5lib")
    for tag in soup.find_all():
        if tag.name in res:
            pass
        else:
            res.append(tag.name)
    print(res)
    print(len(res))
    
#    for ele in aggreagate:
    #if(ele==res):
#    aggreagate.append(res)
#    aggreagate_list.append(url)
 #   webpage_content_analyzer_aggregate(url)
#   else:
#    direct.append(res)
#    direct_list.append(url)
#    webpage_content_analyzer_direct(url)

def webpage_content_analyzer_direct(url):
    if is_executable(url) is True:
        req=requests.get(url)
        print(req)
        #reading the contents of the web page
        html = urlopen(url).read()
        ## print(html)

        soup = BeautifulSoup(html,"html5lib")
        ## print(soup)
        try:
            blocks = soup.find("div",class_="view-content")
            tags=blocks.find("div",class_="item-list")
            tags2=tags.find_all('li')
            for tag in tags2:
                print((tag.get_text()).strip(""))
        except AttributeError as ae:
            print(ae)
            pass
          
def webpage_content_analyzer_aggregate(url):
    if is_executable(url) is True:
        req=requests.get(url)
        print(req)
        #reading the contents of the web page
        html = urlopen(url).read()
        ## print(html)

        soup = BeautifulSoup(html,"html5lib")
        ## print(soup)
        try:
            tbl = soup.find_all('table')
            for tb in tbl:
            #print(tb)
                rows = tb.find_all('tr')
                #print(rows)
                for row in rows:
                    cols = row.find_all('td')
                    #print(cols)
                    for col in cols:
                        hrefs = col.find_all()
                        for href in hrefs:
                            text=href.get_text()
                            print(text)
                    print('\n')
        except AttributeError as ae:
            print(ae)
            pass

for url in urls: #in search(query, tld="co.in", num=1, stop=1, pause=2):
    webpage_type_analyzer(url)
    webpage_content_analyzer_aggregate(url)
    webpage_content_analyzer_direct(url)

#print(aggreagate)
#print(aggreagate_list)
#print(direct)
#print(direct_list)
