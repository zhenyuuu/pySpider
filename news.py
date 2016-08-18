# -*- coding:utf-8 -*-





import urllib
import urllib2
import re
from bs4 import BeautifulSoup
url = 'http://news.baidu.com/' 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('gbk')
soup = BeautifulSoup(content)
print soup.body.str


hotNews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
'''
for i in hotNews:

    print i.a.text

    print i.a['href']






