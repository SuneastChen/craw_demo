from urllib.parse import urlencode,quote
#from urllib import urlencode  py2中如此调用
d = {'name1':'www.pythontab.com','name2':'bbs.pythontab.com'}
print(urlencode(d))
#---->>name2=bbs.pythontab.com&name1=www.pythontab.com

str1 = u'中文网'
str1_encode = str1.encode('utf-8')
d = {'name':str1_encode}
q = urlencode(d)
print(q)
#---->>name=%E4%B8%AD%E6%96%87%E7%BD%91

a = "中文网"
a_urlencode=quote(a)
print(a_urlencode)
#---->>%E4%B8%AD%E6%96%87%E7%BD%91