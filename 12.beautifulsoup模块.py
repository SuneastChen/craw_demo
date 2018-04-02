
import urllib.request


url='http://jandan.net/ooxx/'

req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
response=urllib.request.urlopen (req)
html=response.read().decode('utf-8')

print(html)


from bs4 import BeautifulSoup      #BeautifulSoup必须大写
soup=BeautifulSoup(html,'html.parser')  #soup是一个对象
print(type(soup))
#print(soup.prettify())    #标准格式显示

print('-----------------找单个标签--------------------')

a1=soup.meta.attrs
print(a1)      #获得第一个meta标签所有属性值,返回一个字典

a2=soup.img['src']   #获得第一个img的src属性的内容
print(a2)    #获得指定属性的值


print('-----------------.select(在里面找/子标签找)--------------------')

a3=soup.select('img')  #注意加引号,得到标签的所有属性内容,成列表
print(a3)

##a4=soup.select("img['src']")  #注意单双引号
##
##print(a4)             #select括号里面的[]必须是个条件!条件!!!
a4=[]
for i in a3:
    j=i['src']      #取其具体的属性值
    a4.append(j)

print(a4)



a5=soup.select('.view_img_link')
print(a5)      #按类的值查找到所有标签,成列表

a6=soup.select('#comment-3504479')
print(a6)      #按id的值查找,只有一个,成列表

a7=soup.select("div .row .author a")  #组合使用
print(a7)

####a8=soup.select(".comments #comment-3504479")
####print(a8)      可行的

####a9=soup.select("li.author")  #不加空格找不到
####print(a9)

a10=soup.select("li > div > div")    
print(a10)       #只能通过子标签找,不可以孙标签

print('-----------------根据属性的值找标签--------------------')
####a7=soup.select("div .row .author a[target='_blank']")  #组合使用
####print(a7)                       #可行
####a7=soup.select("div .row .author p > img")  
####print(a7)         可行

a11=soup.select("a[class='view_img_link']")
print(a11)       #并且的关系,不是往里找,与以上方法不可混用,成列表


print('-----------------当列表只有一个元素时,继续找标签--------------------')

a12=soup.p
print(a12)    #得到一个p标签对象

print(a12.string)    #得到文字

print(type(a12))    #<class 'bs4.element.Tag'>

a16=a12.select('a')    #只要是一个类就可以继续往下找
print(a16)          #得到a标签列表



a14=a16[1]['href']     #列表转成对象,当对象中再无标签,则可找其属性;当有标签也可找其属性
print(a14)

print('-----------------单个元素,继续找标签--------------------')

a15=soup.p
print(a15)

a16=soup.p.a    #第一个p元素下的a
print(a16)

a17=soup.p.a['href']
print(a17)


#a14=soup.select('p')[0].select('a')[1]['href']   #同上
#总之一句话,对象.select成列表,列表转成对象,再找;  对象.标签 找第一个标签,可以连着往下找













