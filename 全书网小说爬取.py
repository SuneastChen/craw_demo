# encoding=gbk

import requests
import re
import os



def get_content(url):  # ��ȡ��ҳ����
    req = requests.get(url)
    content_byte = req.content
    content = content_byte.decode('gbk',errors='ignore')
    # print(content)
    return content

def make_book_name(content):  # �½�Ŀ¼
    book_name = re.search('<title>(.+?)</title>', content).group(1)
    os.makedirs(book_name)
    return book_name



def get_dict(content):  #����½�url�ͱ��� �б�
    url_title_list = re.findall('<li><a href="(.+?)" title="(.+?)">', content)
    print(url_title_list)
    return url_title_list

def get_chapters(base_url,u):  #���ÿ�µ����� �б�
    url = base_url + u
    chapters = get_content(url)
    chapters_list = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />', chapters)
    # print(chapters_list)
    return chapters_list


def save_text(chapter_list, path, title):  # ����text����
    file_name = os.path.join(path, title)
    with open(file_name + '.txt', 'w') as f:
        for line in chapter_list:
            f.write(line)
            f.write('\n\n')
        print(file_name, '����ɹ�!')


def main(book_num):  # ���������
    num = str(book_num)[0:-3]
    base_url = 'http://www.quanshuwang.com/book/'+num+'/'+str(book_num)+'/'
    content = get_content(base_url)
    book_dir = make_book_name(content)
    url_title_list = get_dict(content)
    for ut in url_title_list:
        chapter_list = get_chapters(base_url, ut[0])
        save_text(chapter_list, book_dir, ut[1])


if __name__ == '__main__':
    main(22236)    # ����������





