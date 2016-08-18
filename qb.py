# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
def lala():
        
        url = 'http://www.qiushibaike.com'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')

        soup = BeautifulSoup(content, "lxml")
        res = soup.find_all('div' , {'class' : 'content'})
        for i in res:
                print i.string
                
        
        
        
        
                
lala()

    


