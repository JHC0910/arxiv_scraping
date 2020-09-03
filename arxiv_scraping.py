import time
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime as dt


URL = "https://arxiv.org/list/hep-ph/new"

def get_source(URL):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/84.0.4147.89 Safari/537.36"}
    return requests.get(URL, headers=headers)

req = get_source(URL)

soup = BeautifulSoup(req.text.encode('utf-8'), "html.parser")

print(soup.title.string)
print(soup.p)

def TITLES(a,b,c):
    Links = []
    articles =  soup.find_all(class_= a)

    for link in articles:
        links = link.select(b)
        links_text = links[c].getText()
        Links.append(links_text)
    return Links

#authors = soup.find_all(class_= "list-authors")
#for members in authors:
#    Auth = members.find_all('a')
#    print(Auth[0].getText())
    
    
f = open('New_articles.txt','w')  
print(dt.now(), file =f)  
for i in range(0,32):
   print("\n" + str(i+1) + ".:" + TITLES("list-identifier","a",0)[i] + TITLES("meta","div",0)[i] + "Authors:" + TITLES("list-authors","a",0)[i] + " and others..." , file = f)

f.close()
