# _*_ coding:utf-8 _*_
#!/usr/bin/python34
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import threading

def get_img_url_list(url):
    #url='http://www.doutula.com/photo/list/?page=2'
    req=requests.get(url)
    html=req.text
    # print(html)
    soup=BeautifulSoup(html,'lxml')
    img_list=soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})
    img_url_list=[]
    for i in img_list:
        img_url_list.append(i.attrs.get('data-original'))
    return img_url_list

def save_img(img_url):
    # img_url='http://ww2.sinaimg.cn/bmiddle/9150e4e5ly1fjvojsdgczg208c08ct9p.gif'
    img_name=img_url.split('/')[-1]
    # print(img_name)
    save_img_url=os.path.join('img',img_name)
    # print(save_img_url)
    urlretrieve(img_url,save_img_url)    #保存图片
    print('成功保存',img_name)



def get_page_url(page):
    base_url='http://www.doutula.com/photo/list/?page='
    page_url_list=[]
    for i in range(1,page):
        page_url=base_url+str(i)
        # print(page_url)
        page_url_list.append(page_url)
    return page_url_list


def main(page):
    page_url_list=get_page_url(page)
    for p in page_url_list:
        img_url_list=get_img_url_list(p)
        # for i in img_url_list:
        #     save_img(i)
        for i in img_url_list:
            t=threading.Thread(target=save_img,args=[i])
            t.setDaemon(True)   #主线程结束时,子线程还未完成,则都结束
            t.start()

if __name__ == '__main__':
    main(5)
