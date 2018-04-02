import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlretrieve
import threading
import re

def get_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    content = requests.get(url, headers=headers).text
    return content

def get_pages(content):
    soup = BeautifulSoup(content,'lxml')
    pages = len(soup.find_all('a',class_='pagingBar_page'))
    if pages == 0:
        pages = 2
    return pages

def get_h1(content):
    soup = BeautifulSoup(content,'lxml')
    return(soup.find('div',class_='detailContent_title').text)


def get_souds_url_list(page_url):
    page_content = get_content(page_url)
    soup =BeautifulSoup(page_content,'lxml')
    souds_ids_list = soup.find('div',class_='personal_body')['sound_ids'].split(',')
    souds_jsonurl_list = ['http://www.ximalaya.com/tracks/{}.json'.format(id) for id in souds_ids_list]
    souds_url_list =[]
    for soud_jsonurl in souds_jsonurl_list:
        json_content = json.loads(get_content(soud_jsonurl))
        soud_dict={}
        soud_dict['title'] = json_content['title']
        soud_dict['soud_url'] = json_content['play_path']
        souds_url_list.append(soud_dict)
    return souds_url_list
        
def save_soud(soud,h1):  
    houz = soud['soud_url'].split('.')[-1]
    title = re.sub(r'[/\\:*?<>|]','',soud['title'])
    urlretrieve(soud['soud_url'],h1+'/'+title+'.'+houz)
    print(soud['title'],'保存成功!')



def main(url):
    # url = 'http://www.ximalaya.com/54583137/album/4735422/'
    # url = 'http://www.ximalaya.com/2629577/album/203355/'
    content = get_content(url)
    h1 = get_h1(content)
    os.makedirs(h1)
    pages = get_pages(content)
    for page_url in [url + '?page={}'.format(i) for i in range(1, pages)]:
        souds_url_list = get_souds_url_list(page_url)
        # print(souds_url_list)
        for soud in souds_url_list:
                t=threading.Thread(target=save_soud,args=[soud,h1])
                while 1:    #进入判断循环
                    if threading.activeCount()<=10:   
                        #只有当前的激活线程小于6(包括主线程),才会开始
                        t.start()
                        break
        print(page_url,'保存完了')
        print('------------------------------------')


if __name__ == '__main__':
    main('http://www.ximalaya.com/54583137/album/4735422/')