import email
import poplib
import sys
import imp

# imp.reload(sys)
# sys.setdefaultencoding('gbk')

p=poplib.POP3('pop3.163.com')
print(p.getwelcome()+'\n')

p.user('15161580934')
p.pass_('163yx789.')
msg_ct,mbox_siz=p.stat()
rsp,message,msgsiz=p.retr(msg_ct)
mail=email.message_from_string('\r\n'.join(message))
Subject=email.Header.decode_header(mail.get('subject'))[0][0]

From=email.utils.parseaddr(mail.get('from'))[1]
To=email.utils.parseaddr(mail.get('to'))[1]

print('Subject:',Subject)
print('From:',From)
print('To:',To)

for each in mail.walk():
    if not each.is_multipart():
        if each.get_content_type()=='text/plain':
            content=each.get_payload(decode=True)
            print('content:',content)
p.quit()