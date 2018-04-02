import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import threading

def get_content(page_url):
    req = requests.get(page_url)
    content = req.text
    # print(content)
    return content

def get_dict(content):
    title_url_dict = {}
    soup = BeautifulSoup(content, 'lxml')
    div_list = soup.find_all('div', attrs={'class': 'j-video-c'})
    # print(div_list)
    for div in div_list:
        title = div['data-title']
        mp4_url = div.find('div', attrs={'class': 'j-video'})['data-mp4']
        title_url_dict[title] = mp4_url
    print(title_url_dict)
    return title_url_dict

def save_mp4(title, url):
    houz = url.split('.')[-1]
    path = os.path.join('百思不得解视频', title)
    urlretrieve(url, path + '.' + houz)
    print('成功保存!' + title)


def main():
    page_url_list = ['http://www.budejie.com/video/{}'.format(i) for i in range(1, 3)]
    for page in page_url_list:
        print(page)
        content = get_content(page)
        title_url_dict = get_dict(content)

        # 多线程爬取
        for t, u in title_url_dict.items():  # title_url_dict.items()为参数列表
            th = threading.Thread(target=save_mp4, args=[t, u])
            while 1:  # 进入判断循环
                if threading.activeCount() <= 10:
                    # 只有当前的激活线程小于10(包括主线程),才会开始
                    th.start()
                    break


if __name__ == '__main__':
    main()

