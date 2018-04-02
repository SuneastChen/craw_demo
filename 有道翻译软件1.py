import urllib.request
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.sogou.com/sie'
#Network--all--第一个---Headers---General 中可以找到翻译的网址




#将data转成字典,Hearders---Form Data
data='''i:I love Fishc.com!
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
typoResult:true'''
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

import easygui as eg

j[0]=eg.textbox(msg='请输入需要我翻译的内容吧:',title='自动翻译',text='',codebox=0) 
data_dict=dict(zip(i,j))
print(data_dict)



import urllib.parse
data=urllib.parse.urlencode(data_dict).encode('utf-8')   #utf-8转成unicode
req=urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')  #转成utf-8
print(html)      










##print(result)

##eg.textbox(msg='你输入的内容为:%s'%j[0],title='翻译结果...',text=result,codebox=0)   #codebox=0 设置为自动换行
'''
{"translateResult":[[{"tgt":"运行","src":"run"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 奔跑；赛跑；趋向；奔跑的路程\r\n","vt. 管理，经营；运行；参赛\r\n","vi. 经营；奔跑；运转\r\n"],"type":1}}

{"translateResult":[[{"tgt":"happy","src":"快乐"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","happy\r\n","gay\r\n","cheerful\r\n"],"type":1}}

'''







