import mailer

host='smtp.163.com'
sender='15161580934@163.com'
pwd='163yx789.'
receiver='1050521852@qq.com'

message=mailer.Message(From=sender,To=receiver,charset='utf-8')
message.Subject='发个小邮件'
#message.Body='你好啊,This is my first email by python'
message.Html="""This is email uses <strong>HTML</strong><h1>你好啊,This is my first email by python</h1>!"""
message.attach('QQ图片.jpg')

sender=mailer.Mailer(host=host,usr=sender,pwd=pwd)
sender.send(message)
print('邮件发送成功!')