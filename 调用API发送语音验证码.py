#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib.request
from urllib.parse import urlencode
 
#----------------------------------
# 语音验证码调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/61
#----------------------------------
 
def main():
 
    #配置您申请的APPKey
    appkey = "11c126aa7aa2a29084f1703ee0cef67e"
 
    #1.发送语音验证码
    request1(appkey,"GET")
 
 
 
#发送语音验证码
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/yuntongxun/voice"
    params = {
        "valicode" : "abcd1234", #验证码内容，字母、数字 4-8位
        "to" : "15161580934", #接收手机号码
        "playtimes" : "3", #验证码播放次数，默认3
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
 
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)
 
    content = f.read().decode('utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print(res["result"])
        else:
            print ("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print ("request api error")
 
 
 
if __name__ == '__main__':
    main()