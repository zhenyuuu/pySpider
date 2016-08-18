
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import xlwt



baseurl = "https://book.douban.com/top250?start=25"


url = baseurl
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {"User_Agent" : user_agent}
request = urllib2.Request(url,headers = header)
response = urllib2.urlopen(request)
content = response.read()
soup = BeautifulSoup(content,"lxml")

table = soup.find_all('table', width="100%")

a = len(table)
for i in range(a-1):
    sp = BeautifulSoup(str(table[i-1]) , 'lxml')
    bookname = sp.div.a['title']
    bookhref = sp.div.a['href']
    bookinfo = sp.find('p',{"class" :"pl"}).string
    #print bookname,bookhref,bookinfo
    nickname =  sp.div.span
    if (nickname):
        nickname = nickname.string
    else:
        nickname = "none"
    bookrank = sp.find('span', class_= 'rating_nums').string
    num = sp.find('span', class_="pl").string
    num = num.replace(' ','').replace('\n','').strip()
    imageurl = sp.img['src']
    print num
    #download_img(imageurl,bookname)
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet1 = workbook.add_sheet("top 250", cell_overwrite_ok=True)
    item = ["书名","别称" ,"链接" ,"信息" ,"评分"]
    for i in range(4):
        sheet1.write(0,i+1,item[i])
        for j in range(1,25):
            writelist = [j,bookname,nickname,bookhref,bookinfo,bookrank]
            for k in range(4):
                sheet1.write(i+j,k,writelist[k])
workbook.save("D:\\booktop250.xls")
print '10'
        
    
    
    
    
    



print "10"  
                      
                      
		      



