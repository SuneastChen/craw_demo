print('----------------爬妹子---------------')

import os
import urllib.request
from bs4 import BeautifulSoup

def url_open(url):    #打开网页,获得网页源码
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    response=urllib.request.urlopen (req)
    html=response.read()
    return html



def get_page(url):    #获得总页数
    html=url_open(url).decode('utf-8')

    soup=BeautifulSoup(html,"html.parser")
#    page1=soup.select('div > div > span')
    page1=soup.select('#wrapper #body div > div span[class=current-comment-page]') #都可以混合使用
    page2=page1[0].string
    page2=page2.strip('[')
    page2=page2.strip(']')
    return page2


def get_imgaddrs(url):      #得到图片的url列表

    html=url_open(url).decode('utf-8')

    soup=BeautifulSoup(html,"html.parser")

    imgs_list=soup.select('.text p img')  
    imgs_addrs=[]
    for i in imgs_list:
        if i.attrs.get('org_src'):
            imgs_addrs.append(i['org_src'])
        elif str(i['src'])[:6] != 'http:':            
            imgs_addrs.append(i['src'])
    return imgs_addrs


##print(get_imgaddrs('http://jandan.net/ooxx/page-177#comments'))        




url='http://jandan.net/ooxx/'
page_num=int(get_page(url))
print(page_num)     


os.mkdir('xxoo')     #创建一个文件夹
os.chdir('xxoo')     #改变工作目录

for j in range(5):
    page_num-=j
    page_url=url+'page-'+str(page_num)+'#comments'
    imglist=get_imgaddrs(page_url)
    print(imglist)
    for i in imglist:
        i='http:'+i
        
        img=url_open(i)
        filename=i.split('/')[-1]
        with open(filename,'wb') as f:
            f.write(img)














