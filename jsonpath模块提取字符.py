import requests
import json
import jsonpath
import chardet

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
req = requests.get(url,headers=headers)
html = req.text
print(chardet.detect(req.content))

py_dict = json.loads(html)


citys = jsonpath.jsonpath(py_dict,'$..name')  # 返回匹配成功的字符串列表
print(citys)