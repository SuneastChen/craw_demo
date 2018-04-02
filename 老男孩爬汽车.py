import urllib.request
from bs4 import BeautifulSoup

url='http://www.autohome.com.cn/news/'
# data_dict={}    #上传的数据
# data=urllib.parse.urlencode(data_dict).encode('utf-8')   #utf-8转成unicode
head={}    #伪造客户端的头部信息,head在之Request对象生成之前
head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

req=urllib.request.Request(url,headers=head)  #Request必须用大写,得到一个Request对象
response=urllib.request.urlopen(req)    #传入一个对象,返回一个对象
html=response.read().decode('gbk')     #转成utf-8可认识的信息
# print(html)


soup=BeautifulSoup(html,features='html.parser')
target=soup.find(id='auto-channel-lazyload-article')   #gbk的网页格式不可直接复制其网页内容,会出现编码问题
li_list=target.find_all('li')
# print(li_list)
# 
# 
# 
import os
os.mkdir('.\\car')

for i in li_list:
	a=i.find('a')
	# print(a)
	if a:     #有的li里面根本无a标签
		print(a.attrs.get('href'))   #或a['href']也可以
		txt=a.find('h3').text     #spring/text都可以
		print(txt)
		img_url=a.find('img')['src']
		print(img_url)

		head={}    #伪造客户端的头部信息,head在之Request对象生成之前
		head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

		req=urllib.request.Request(img_url,headers=head)  #Request必须用大写,得到一个Request对象
		response=urllib.request.urlopen(req)    #传入一个对象,返回一个对象
		img_b=response.read()  #img_b为二进制

		import uuid
		img_name=str(uuid.uuid4())+'.jpg'
		with open('./car/'+img_name,'wb') as f:    #必须用二进制可写模式
			f.write(img_b)