# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

the_html="""
<a href="aaaas"><img src="saaa"/></a>
<a class="url" href="saasa">那个分享第二份职业，两个月...</a>
<a href="aaaaa"><img src="aaaaa"></a>
<a class="url" href="aaaaa">兼职一：这是一个在手机上赚...</a>
<a href="saa">缁欐垜鍏虫敞鐨勪汉鍐欎俊</a>
<a href="saaaat">鍘绘垜鍏虫敞鐨勪汉鍒楄〃</a>
"""

soup=BeautifulSoup(the_html)
a = soup.find_all("a",{"href" : True})

for one in a:
    print one.get("href")                        
