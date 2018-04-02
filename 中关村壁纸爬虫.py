import requests
from urllib.request import urlretrieve
import re
import os
import threading

def get_page_url(classes, subclass, page):
    page_url_list = ['http://desk.zol.com.cn/{}/{}/{}.html'.format(classes, subclass, i) for i in range(1, page)]
    print(page_url_list)
    return page_url_list

def get_content(url):
    req = requests.get(url)
    content_bytes = req.content
    content = content_bytes.decode('gbk')
    # print(content)
    return content

def get_imagesurl_title(html):
    imagesurl_title_list = re.findall('<li class="photo-list-padding"><a class="pic" href="(.+?)" \
target="_blank" hidefocus="true"><img width="208px" height="130px"  alt="(.+?)"', html)
    print(imagesurl_title_list)
    return imagesurl_title_list

def make_title_dir(title):
    save_images_dir = r'./中关村壁纸/%s' % title
    os.makedirs(save_images_dir)
    return save_images_dir


def get_imgs_url_list(html):
    imgs_url_list = re.findall('<img srcs?="(.+?)" width="144" height="90"', html)
    return imgs_url_list

def save_img(img_url, file_name):
    urlretrieve(img_url, file_name)



def main(classes, subclass='p4', page=2):
    page_url_list = get_page_url(classes, subclass, page)
    for page_url in page_url_list:
        content = get_content(page_url)
        imagesurl_title_list = get_imagesurl_title(content)
        for iu_t in imagesurl_title_list:
            save_images_dir = make_title_dir(iu_t[1])
            imagesurl = 'http://desk.zol.com.cn'+iu_t[0]
            images_content = get_content(imagesurl)
            imgs_url_list = get_imgs_url_list(images_content)
            # print(imgs_url_list)
            s = 0
            for img_url in imgs_url_list:
                img_url = img_url.replace('144x90', '1377x768')
                houzui = img_url.split('.')[-1]
                s += 1
                file_name = save_images_dir+'/'+str(s)+'.'+str(houzui)

                t = threading.Thread(target=save_img, args=[img_url, file_name])
                while 1:  # 进入判断循环
                    if threading.activeCount() <= 10:
                        # 只有当前的激活线程小于10(包括主线程),才会开始
                        t.setDaemon(True)
                        t.start()
                        break

            print('保存成功!', iu_t[1])

if __name__ == '__main__':
    main('meinv')

