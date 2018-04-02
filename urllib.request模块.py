import urllib.request

'''
newsurl='http://www.fishc.com'
response=urllib.request.urlopen(newsurl)    #得到一个object
html=response.read()
#print(response.read())    #得到16进制网页数据

html=html.decode('utf-8')   #转成'utf-8'可认识的html
print(html)




print('----------------保存了只猫的图片---------------')
response=urllib.request.urlopen('http://placekitten.com/g/400/400')
cat=response.read()
with open('cat.jpg','wb')  as f:
    f.write(cat)

#完整的写法
req=urllib.request.Request('http://placekitten.com/g/400/400')  #Request必须用大写
response=urllib.request.urlopen(req)    #传入一个对象,返回一个对象
cat=response.read()
with open('cat.jpg','wb')  as f:
    f.write(cat)
print(response.geturl())    #得到网址
print(response.info())      #得到head信息
print(response.getcode())     #得到网页状态





print('----------------有道词点翻译---------------')

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.sogou.com/sie'
#Network--all--第一个---Headers---General 中可以找到翻译的网址
##head={}       #head在之Request对象生成之前加入
##head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'


#将data转成字典,Hearders---Form Data
data={}
'i:I love Fishc.com!
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:1499579386799
sign:9c23980e3623e9c1fcfb445190cf8337
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_CL1CKBUTTON
typoResult:true'
data=data.replace ('\n',':')  #先把\n替换成:
data_list=data.split(':')    #以:分割成列表
#print(data_list)

i=[]
j=[]
for a in data_list:
    if data_list.index(a)%2==0:
        i.append(a)
    else:
        j.append(a)

#print(i)
#print(j)
#j[0]=input('输入要翻译的内容:')

data_dict=dict(zip(i,j))
print(data_dict)





import urllib.parse
data=urllib.parse.urlencode(data_dict).encode('utf-8')   #utf-8转成unicode
req=urllib.request.Request(url,data)
#head在之Request对象生成之后加入
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')  #转成utf-8
#print(html)
#{"translateResult":[[{"tgt":"我爱Fishc.com !","src":"I love Fishc.com!"}]],"errorCode":0,"type":"en2zh-CHS"}


import json
target=json.loads(html)
result=target["translateResult"][0][0]['tgt']
print(result)



print('----------------代理IP---------------')

import random
#过度频繁地访问服务器,解决办法,1.import time 2.使用代理IP

url='http://www.ipdizhichaxun.com/'

iplist=['118.193.23.162:3128','118.144.154.253:3128','119.36.92.41:80']

#1.参数是一个字典
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
#2.定制,创建一个opener
opener=urllib.request.build_opener(proxy_support)
#加入头信息,用元组的列表
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')] 
#3.安装一个opener
urllib.request.install_opener(opener)
#4不想用代理时,opener.open(url)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)



print('----------------爬妹子---------------')

import os
import urllib.request
from bs4 import BeautifulSoup 

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    response=urllib.request.urlopen (req)
    html=response.read()
    return html



def get_page(url):
    html=url_open(url).decode('utf-8')

    soup=BeautifulSoup(html,"html.parser")
#    page1=soup.select('div > div > span')
    page1=soup.select('#wrapper #body div > div span[class=current-comment-page]') #都可以混合使用
    page2=page1[0].string
    page2=page2.strip('[')
    page2=page2.strip(']')
    return page2

def get_imgaddrs(url):

    html=url_open(url).decode('utf-8')

    soup=BeautifulSoup(html,"html.parser")

    imgs_list=soup.select('.text p img')  #只能从div块级元素开始找
    imgs_addrs=[]
    for i in imgs_list:
        imgs_addrs.append(i['src'])
    return imgs_addrs


##print(get_imgaddrs('http://jandan.net/ooxx/page-177#comments'))        




url='http://jandan.net/ooxx/'
page_num=int(get_page(url))
print(page_num)

      


os.mkdir('xxoo')     #创建一个文件夹
os.chdir('xxoo')     #改变工作目录

for j in range(3):
    page_num-=j
    page_url=url+'page-'+str(page_num)+'#comments'
    imglist=get_imgaddrs(page_url)
    
    for i in imglist:
        i='http:'+i
        
        img=url_open(i)
        filename=i.split('/')[-1]
        with open(filename,'wb') as f:
            f.write(img)

'''
print('----------------------urlretrieve-------------------------')

#urlretrieve(url, filename=None, reporthook=None(回调函数), data=None)

urllib.request.urlretrieve("http://wx2.sinaimg.cn/mw600/005vbOHfgy1fht13rocy5j30g40lhmyy.jpg","123.jpg")
# def cbk(a, b, c): 
#     '''回调函数
#     @a: 已经下载的数据块
#     @b: 数据块的大小
#     @c: 远程文件的大小
#     ''' 
#     per = 100.0 * a * b / c 
#     if per > 100: 
#         per = 100 
#     print ('%.2f%%' % per)
 
# url = 'http://wx2.sinaimg.cn/mw600/005vbOHfgy1fht13rocy5j30g40lhmyy.jpg'

# local = 'd://meinv.jpg'
# urllib.request.urlretrieve(url, local, cbk)


print('----------------------异常处理方法1-------------------------')

import urllib.request
from urllib.error import URLError,HTTPError

req=urllib.request.Request('http://www.youdaili.net/')
try:
    response=urllib.request.urlopen(req)
except HTTPError as e:             #一定要先接收HTTPError错误类型,因为HTTPError是URLError的子类
    print('http类型错误,错误状态:%d'%e.code)
    print(e.reason)
    print(e.getcode())
    print(e.__dict__)
#{'name': '<urllib response>', 'fp': <http.client.HTTPResponse object at 0x0000000003042908>, 
#'msg': 'Forbidden', 'url': 'http://www.youdaili.net/', 
#'file': <http.client.HTTPResponse object at 0x0000000003042908>, 
#'hdrs': <http.client.HTTPMessage object at 0x0000000003056860>,
# 'delete': False, 'code': 403, '_closer': <tempfile._TemporaryFileCloser object at 0x0000000003042940>}

except URLError as e:
    print('URLError类型错误,错误原因:%s'%e.reason)
    print(e.__dict__)    #只有一个原因属性
else:
    print('打开正常!')

# URLError有一个reason属性
# httpError有一个code属性,100-299成功,300-399自动处理,400-499客户端问题,500-599服务器问题

print('----------------------异常处理方法2,推荐使用-------------------------')
from urllib.request import Request,urlopen
from urllib.error import URLError
req=Request('http://www.youdaili.net/')
try:
    response=urlopen(req)
except URLError as e:
    if hasattr(e,"reason"):
        print("异常原因为:",e.reason)
    elif hasattr(e,'code'):
        print('状态为:',e.code)
else:
    print('打开正常')































