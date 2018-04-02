from ftplib import FTP
ftp=FTP()
ftp.set_debuglevel(2) #打开调试级别2，可以显示详细信息
ftp.connect('192.168.0.174',21) #连接(IP,端口)
ftp.login('xudong1','xudong1') #登录，如果匿名登录则用空串代替即可
print(ftp.getwelcome()) #显示ftp服务器欢迎信息

# ftp.cwd('xxx/xxx/') #选择操作目录
bufsize = 1024 #设置缓冲块大小
filename='abcde.txt'  #需要下载的文件
file_handler = open(filename,'wb').write #以写模式在本地打开文件
ftp.retrbinary('RETR %s'% filename,file_handler,bufsize) #接收服务器上文件并写入本地文件
ftp.set_debuglevel(0) #关闭调试
ftp.quit() #退出ftp服务器