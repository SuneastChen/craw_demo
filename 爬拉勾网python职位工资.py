
import requests
from bs4 import BeautifulSoup
import time
def main():
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
    # url='https://www.lagou.com/jobs/list_python?px=default&city=%E4%B8%8A%E6%B5%B7#filterBox'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Host': 'www.lagou.com',
            'Origin': 'https: // www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=%E7%88%AC%E8%99%AB',
            'Cookie':'user_trace_token=20170912213445-3ff6bf04-c195-436f-b46c-8accd777ca7f; LGUID=20170912213455-29b5c180-97bf-11e7-9062-525400f775ce; JSESSIONID=ABAAABAAAFCAAEG1D0CA3817C0E4AB796FBD89CD498F760; index_location_city=%E5%85%A8%E5%9B%BD; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB; TG-TRACK-CODE=search_code; SEARCH_ID=ac8a1da1ad734b5788dc233710678e53; X_HTTP_TOKEN=af77bf09d601de725212834ff0e06c90; _gid=GA1.2.1679448328.1511333938; _gat=1; _ga=GA1.2.94886327.1505223288; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511333938; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511339330; LGSID=20171122160349-abdcd8d3-cf5b-11e7-9d19-525400f775ce; LGRID=20171122162851-2ba224df-cf5f-11e7-9986-5254005c3644'
            }

#只爬取第一页时
    '''
    data={'first':'true',
            'pn':'1',      #此代表页数
            'kd':'python'}
    req=requests.post(url,headers=headers,data=data)

#注意事项:
    # req 返回的是json格式
    # bbb=req.content      #直接用content读取内容,未转换成utf-8格式,为字节型
    # sss=req.content.decode('utf-8')      #字节再转换成utf-8格式,就变成字符串了
    # sss=req.text      #直接用text读取内容,未转换成utf-8格式,为字符串型
    dict_result=req.json()    #由json格式转为dict
    positions=dict_result['content']['positionResult']['result']

    print(positions)
    '''
#爬取多页时
    

    # 拉勾网第一次请求要加上一个cookies信息,然后用Session来请求,自动更新cookies
    # 这样请求就不会有限制了
    sess = requests.Session()
    sess.headers.update(headers)

    position_all=[]
    for i in range(1,20):
        print('正在爬取第%d页' % i)
        data = {'first': 'false',
            'pn': i,  # 此代表页数
            'kd': '爬虫'}   # 此代表搜索职位关键字
        res = sess.post(url, data=data, headers=headers)
        dict_result = res.json()       # json格式转为dict
        print(dict_result)
        position = dict_result['content']['positionResult']['result']
        position_all.append(position)
        # time.sleep(5)
        

    print(position_all)







if __name__=='__main__':
    main()