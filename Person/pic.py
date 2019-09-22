#coding=utf-8

import urllib.request
import os
from bs4 import BeautifulSoup

url = 'http://p.weather.com.cn/'

def findallimageurl(htmlstr):
    sp = BeautifulSoup(htmlstr, 'html.parser')
    imgtaglist = sp.find_all('img')
    # print(imgtaglist[0])
    srclist = list(map(lambda u: u.get('src'), imgtaglist))
    filtered_srclist = filter(lambda u: u.lower().endswith('.png') or u.lower().endswith('.jpg'), srclist)
    # print(list(filtered_srclist))
    return filtered_srclist

def getfilename(urlstr):
    pos = urlstr.rfind('/')
    return urlstr[pos+1]

def getpictest():
    url_list = []
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        htmlstr = data.decode()
        url_list = findallimageurl(htmlstr)
        
    # for imagesrc in list(url_list):
        
    #     req = urllib.request.Request(imagesrc)
    #     with urllib.request.urlopen(req) as response:
    #         data = response.read()
    #         if len(data) < 1024 * 100:
    #             continue
            
    #         if not os.path.exists('download'):
    #             os.mkdir('download')

    #         filename = getfilename(imagesrc)
    #         filename = 'download/' + filename
    #         with open(filename,'wb') as f:
    #             f.write(data)
    oneurl = list(url_list)[0]
    req = urllib.request.Request(oneurl)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        
        if not os.path.exists('download'):
            os.mkdir('download')

        filename = getfilename(oneurl)
        filename = 'download/' + filename
        with open(filename,'wb') as f:
            f.write(data)
    print('xiazaitupian', filename)
        


