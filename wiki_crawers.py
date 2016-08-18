import urllib2
import re
from bs4 import BeautifulSoup

import datetime
import random

pages = set()

def getLinks(pageUrl):
    global pages
    request = urllib2.Request("https://en.wikipedia.org" + pageUrl)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    #print soup
    for link in soup.find_all('a', href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print newPage
                pages.add(newPage)
                getLinks(newPage)
        
getLinks('')
    
    
    
