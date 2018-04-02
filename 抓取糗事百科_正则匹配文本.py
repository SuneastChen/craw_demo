import requests
import re

def get_text(page):
    for i in range(1,page+1):
        req=requests.get('https://www.qiushibaike.com/8hr/page/{}/'.format(i))
        html=req.text
        # print(html)
        text_list=re.findall('<div class="content">[\n]<span>(.+?)</span>',html,re.S)
        for text in text_list:
            print(text_list.index(text),text.strip())


get_text(3)
