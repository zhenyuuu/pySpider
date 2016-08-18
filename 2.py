
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sh600000&Page=1'
response = urllib2.urlopen(url).read()
soup = BeautifulSoup(response)
res = soup.find('div', attrs={'class': "datelist"})
ur = res.contents[0]
#print ur
#print ur
ur = list(ur)
for i in ur:
    print i
ur = ur[:-1]
for m in ur:

    print ur
#temp = unicode(ur[0])
"""for index in range(0, len(ur), 4):
    temp = unicode(ur[index])
    print temp.strip()
    print ur[index+1].string
    print ur[index+1]['href']
    print '\n'
"""
