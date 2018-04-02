from bs4 import BeautifulSoup
from urllib import parse
import requests
import csv

url0='http://bj.ganji.com/fang1/'
addr='http://bj.ganji.com'
headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) '}


if __name__=='__main__':
    start_page=0
    end_page=50
    with open('赶集租房信息.csv','w',newline='') as f:
        csv_writer=csv.writer(f,delimiter=',',dialect='excel')
        csv_writer.writerow(['房屋标题', '租房地址', '租房价格', '详情页链接'])
        print('start---------------')
        while start_page < end_page:
            start_page +=1
            url=url0+'o'+str(start_page)
            print(url)
            req=requests.get(url,headers=headers)
            html=BeautifulSoup(req.text,'html.parser')
            # print(html)

            house_list=html.select('.f-list-item  dl[class="f-list-item-wrap f-clear"]')
            # print(house_list)
            if not house_list:
                break
            for house in house_list:
                house_title=house.select('a[class="js-title value title-font"]')[0]['title']
                # print(house_title)
                house_addr=house.select('span[class="area"]')[0].text.replace(' ','').replace('\n','')
                # print(house_addr)
                house_price=house.select('div[class="price"]')[0].text.replace(' ','').replace('\n','')
                # print(house_price)

                house_url=house.select('a[class="js-title value title-font"]')[0]['href']
                if house_url.startswith('/fang'):
                    house_url=addr+house_url
                # print(house_url)

                csv_writer.writerow([house_title,house_addr,house_price,house_url])
    print('end----------------')




