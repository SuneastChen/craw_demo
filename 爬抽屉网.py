import requests
r1=requests.get('http://dig.chouti.com/')
r1_cookies=r1.cookies.get_dict()

post_dict={
	'phone':'8615161580934',
	'password':'chouti',
	'oneMonth':1
}

r2=requests.post(
	url='http://dig.chouti.com/login',
	data=post_dict,
	cookies=r1_cookies
	)

r3=requests.post(
	url='http://dig.chouti.com/link/vote?linksId=13816736',\
	cookies={'gpsd':r1_cookies.get('gpsd')}
)
print(r3.text)