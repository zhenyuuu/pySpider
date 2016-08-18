

# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup




baseurl = "https://book.douban.com/top250?start=25"


url = baseurl
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {"User_Agent" : user_agent}
request = urllib2.Request(url,headers = header)
response = urllib2.urlopen(request)
content = response.read()
soup = BeautifulSoup(content,"lxml")
bookname = soup.find_all('div',class_ = "pl2")
for i in bookname:
    c= str(i)
    a = BeautifulSoup(c)
    b= a.string[0]

    print a
    print b

