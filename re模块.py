import re

a1='高位控制abc123'
a2=re.findall(r'[a-z]',a1)
print (a2)     #['a', 'b', 'c']找到所有返回一个列表

a3=re.search(r'[a-z]',a1)
print(a3)    #<_sre.SRE_Match object; span=(4, 5), match='a'>
#print(re.__doc__)
print("\b")   #退格符

str1 = 'dit dot det,dct dit dot'
print (re.findall('dit',str1))   #['dit', 'dit']

print (re.findall('dit|dct',str1)) #['dit', 'dct', 'dit']
print (re.findall('d[ic]t',str1))  #['dit', 'dct', 'dit']
print (re.findall('d[^ic]t',str1)) #['dot', 'det', 'dot']
print (re.findall('^dit',str1))    #['dit']
print (re.findall('dot$',str1))    #['dot']
print (re.findall('d.+t',str1))  #['dit dot det,dct dit dot']

str1 = 'd dt dit diit det'
print(re.findall('d.+t',str1))  #['d dt dit diit det']  贪婪模式
print (re.findall('d.+?t',str1))   #['d dt', 'dit', 'diit', 'det']  非贪婪模式
print (re.findall('di*t',str1))  #['dt', 'dit', 'diit']  di*t表示d与t之间省略了零个至多个'i'
print (re.findall('di?t',str1))  #['dt', 'dit']  di?t表示i可有可无，即dt、dit都满足匹配条件

str1 = 'dt dit diit diiit diiiit'
print (re.findall('di{2}t',str1))  #['diit']
print (re.findall('di{1,3}t',str1))  #['dit', 'diit', 'diiit']  di{n,m}t表示d和t之间有n到m个'i'
#其中，n和m都是可以省略的。{n,}表示n个到任意个；{,m}表示0个到m个；{,}表示任意个，和'*'功能一样

print('--------------转译符-------------------')
str1 = '^abc ^abc'
print (re.findall('^abc',str1))   #[]
print (re.findall('\^abc',str1))  #['^abc', '^abc']


print('--------------预定义字符-------------------')
str1 = '12 abc 345 efgh'
print (re.findall('\d+',str1))   #['12', '345']
print (re.findall('\w+',str1))   #['12', 'abc', '345', 'efgh']


p=re.compile(r'[a-z]',re.I)   #作用：把正则表达式语法转化成正则表达式对象
a4=p.search('I love Fishc.com')  
print(a4)  #<_sre.SRE_Match object; span=(2, 3), match='l'>
print(a4.group())



#()作用：在匹配字符串后，只输出匹配字串'()'里面的内容：

str1 = '12abcd34'
print (re.findall('12abcd34',str1))      #['12abcd34']
print (re.findall('1(2a)bcd34',str1))    #['2a']
print (re.findall('1(2a)bc(d3)4',str1))  #[('2a', 'd3')]


print('--------------re模块里的主要方法-------------------')

#re模块里的主要方法：findall()、finditer()、match()、search()、compile()、split()、sub()、subn()
#re.findall(pattern,string,flags = 0) 在string中从左往右搜索与pattern匹配的字串，结果以list形式返回
str1 = 'ab cd'
print (re.findall('\w+',str1))  #['ab', 'cd']

#re.finditer(pattern,string,flags = 0) 其功能与re.findall相同，但结果以迭代器的形式返回
str1 = 'ab cd'
iter1 = re.finditer('\w+',str1)
for a in iter1:
    print (a.group(),a.span())   #ab (0, 2)    cd (3, 5)
#注：a.group()返回满足匹配调节的字串，a.span()返回字串的起始位置和末尾位置


#re.search(pattern,string,flags = 0) 在string中从左往右搜索与pattern匹配的字串，无匹配结果则返回None，否则返回一个search实例
str1 = 'cd cd'
result = re.search('cd',str1)
if result == None:
 	 print ('None')      #无匹配结果不可用下面的group(),start(),end()
else:
  	print (result.group(),result.start(),result.end())    #只返回符合条件的第一个


#re.match(pattern,string,flags = 0)  判断string的头部是否与pattern匹配，是则返回match实例，否则返回None
print("---------")
str1 = 'ab cd'
result = re.match('cd',str1)
if result == None:
 	 print ('None')      #无匹配结果不可用下面的group(),start(),end()
else:
  	print (result.group(),result.start(),result.end())     #ab 0 2

#re.compile(pattern,flags = 0)  对匹配格式pattern进行编译，返回一个实例对象。对正则表达式先编译，可以大幅提高匹配速度
str1 = 'ab cd'
pre = re.compile('ab')
print (pre.findall(str1))


#re.split(pattern,string,maxsplit = 0,flags = 0)   在string匹配pattern的时候以string做为分割,string没了
str1 = 'ab.c.de'
str2 = '12+34-56*78/90'
print (re.split('\.',str1))    #['ab', 'c', 'de']
print (re.split('[\+\-\*/]',str2))    #['12', '34', '56', '78', '90']


#re.sub(pattern,repl,string,count = 0,flags = 0)   查找到替换,返回替换后的字符串,在string当中把满足pattern正则的字串替换成repl
str1 = 'abcde'
print (re.sub('bc','123',str1))    #a123de


#re.subn(pattern,repl,string,count = 0,flags = 0)   功能与re.sub()相同，但返回的结果多了一个数字，代表替换了多少次
str1 = 'abcdebce'
print (re.subn('bc','123',str1))     #('a123de123e', 2)


print('--------------断言-------------------')
str3='love you,love xiaoming,love fishc.com,123 fishc,456 fishc'
b1=re.findall("love(?= fishc)",str3)     #['love']  向前肯定断言,只能匹配后面跟 fishc的love
print(b1)

b2=re.findall('love(?! fishc)',str3)    #['love', 'love'] 向前否定断言
print(b2)

b3=re.findall('(?<=love) fishc',str3)    #[' fishc'] 向后肯定断言,只能匹配前面有love的 fishc
print(b3)

b4=re.findall('(?<!love) fishc',str3)    #[' fishc', ' fishc']向后否定断言
print(b4)


print('--------------获取IP-------------------')

import urllib.request
import re

def open_url(url):
		#data_dict={}    #上传的数据
		#data=urllib.parse.urlencode(data_dict).encode('utf-8')   #utf-8转成unicode
		head={}    #伪造客户端的头部信息,head在之Request对象生成之前
		head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
                         #   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0
		req=urllib.request.Request(url,headers=head)  #Request必须用大写,得到一个Request对象
		response=urllib.request.urlopen(req)    #传入一个对象,返回一个对象
		html=response.read().decode('utf-8')     #转成utf-8可认识的信息
		return html

def get_ip(html):
	p=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td>\s+?<td>\d{1,4}'
	iplist=re.findall(p,html)
	for i in iplist:
		print(re.sub(r'</td>\s+?<td>',':',i))      #使用正则替换
	

if __name__=='__main__':
	url='http://www.xicidaili.com/nn/'
	get_ip(open_url(url))