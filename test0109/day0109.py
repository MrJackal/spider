#-- coding:utf-8 --
'''
Created on 2020.1.9

@author: liuchunlei01
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

'''
html = urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read(),"html.parser");
print(bsObj.img['src'])

#获取网页标题的方法，主要是try的方式，保证系统正常运行
def getTitle(url):
    try:
        html = urlopen(url, None, 6000)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.title;
    except AttributeError as e:
        print(e)
        return None;
    return title;

title = getTitle("http://www.baidu.com")
print(title)
'''

#获取网页之后根据网页的内容，获取想要的值

html2 = urlopen("https://www.ln80.cn", None, 6 * 1000)
page = BeautifulSoup(html2.read(),"html.parser")
print(page)

    
