import requests
import json
import urllib
#city=inpurt(请输入要查询天气的城市名>>)
city='南京'
# city_encode=urllib.parse.quote(city)
# print(city_encode)
# url='http://v.juhe.cn/weather/index?format=2&cityname='+city_encode+'&key=c5473f76bb00946d760d90730dcd38c1'
url='http://v.juhe.cn/weather/index?format=2&cityname='+city+'&key=c5473f76bb00946d760d90730dcd38c1'
req=requests.get(url)
result_dict=json.loads(req.text)


today=result_dict['result']['today']['date_y']
city=result_dict['result']['today']['city']
temperature=result_dict['result']['today']['temperature']
weather=result_dict['result']['today']['weather']
dressing_index=result_dict['result']['today']['dressing_index']
dressing_advice=result_dict['result']['today']['dressing_advice']

print('今天是',today,'您所在的城市是',city,'\n',\
    '今天的温度为',temperature,'天气情况是',weather,'\n',\
    '今天整体状况是',dressing_index,'\n',\
    '所以啊',dressing_advice)



