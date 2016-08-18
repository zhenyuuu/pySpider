#!/usr/bin/python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib2


def askURL(url):
    request = urllib2.Request(url)#发送请求
    try:
        response = urllib2.urlopen(request)#取得响应
        html= response.read()#获取网页内容
        #print html
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    return html
def getData(url):
    for i in range(0,10):
        baseurl = url +str(i*25)
        html = askURL(baseurl)
        soup = BeautifulSoup(html , "lxml")
        movietitle = soup.find_all('span',class_ = "title")
        movieinfo = soup.find_all('p')
        movierate = soup.find_all('div' , class_ = 'rating_num')
        movienum = soup.find_all('span', class_ = None)
        movieintr = soup.find_all('span', class_ = 'inq')
        moviesrc = soup.find_all('a')
        
        for i in range(0,25):

            print movietitle[i].string
            a = movieinfo[i].contents[1]
            b= movieinfo[i].contents.append(a)
            print b
            
        

    
    
getData("https://movie.douban.com/top250?start=")
