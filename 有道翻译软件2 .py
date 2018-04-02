import requests
import time
import random
import hashlib
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
#Network--all--第一个---Headers---General 中可以找到翻译的网址

import easygui as eg

contents=eg.textbox(msg='请输入需要我翻译的内容吧:',title='自动翻译',text='',codebox=0) 


#post的data分析,每次salt,sign的值不同
# js中的源码分析:
# salt: f,
# f = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
timestamp=int(time.time()*1000)+random.randint(0,10)

# sign: g,
# var g = n.md5(u + d + f + c);
# u = "fanyideskweb",
# d = a.val(),  i=d   已知i为要翻译的值--->>故d为要翻译的值
# f = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
# c = i.deEight("rY0D^0'nM0}g5Mm1z%1G4"),
# deEight()为一个函数
# deEight: function(e) {
#             var t, n = new Array,
#             r = e.split("\\");
#             if (1 == r.length) return r[0];
#             for (t = 1; t < r.length; t++) n += String.fromCharCode(parseInt(r[t], 8));
#             return e = n
#         }
#故c='rY0D^0'nM0}g5Mm1z%1G4'
u='fanyideskweb'
d=contents
f=str(timestamp)
c="rY0D^0'nM0}g5Mm1z%1G4"
sign=hashlib.md5((u+d+f+c).encode('utf-8')).hexdigest()
print(c)
print(contents)
print(timestamp)
print(sign)

data={'i':contents,
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':timestamp,
'sign':sign,
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_CL1CKBUTTON',
'typoResult':'true'}
# print(data)

import urllib.parse
data=urllib.parse.urlencode(data).encode('utf-8')   #utf-8转成unicode
req=urllib.request.Request(url,method='POST',data=data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')  #转成utf-8
print(html)      

# req=requests.post(url,data=data)

# print(req.text)






##print(result)

##eg.textbox(msg='你输入的内容为:%s'%j[0],title='翻译结果...',text=result,codebox=0)   #codebox=0 设置为自动换行
'''
{"translateResult":[[{"tgt":"运行","src":"run"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 奔跑；赛跑；趋向；奔跑的路程\r\n","vt. 管理，经营；运行；参赛\r\n","vi. 经营；奔跑；运转\r\n"],"type":1}}

{"translateResult":[[{"tgt":"happy","src":"快乐"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","happy\r\n","gay\r\n","cheerful\r\n"],"type":1}}

'''







