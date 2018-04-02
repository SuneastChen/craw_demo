from ftplib import FTP
ftp=FTP()
ftp.set_debuglevel(2)
ftp.connect('192.168.0.174',21)
ftp.login('xudong1','xudong1')
print(ftp.getwelcome())

# ftp.cwd('xxx/xxx/')
bufsize = 1024
filename='1234.txt'
file_handler = open(filename,'rb')
ftp.storbinary('STOR %s'%filename,file_handler,bufsize) #上传文件
ftp.set_debuglevel(0)
file_handler.close() #关闭文件
ftp.quit()