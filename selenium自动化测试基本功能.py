# _*_ coding:utf-8 _*_
#!/usr/bin/python34

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()  # 也可换成Ie()，Firefox(),Chrome等
driver.get('http://www.baidu.com/')




def get_ele_times(driver,times,func):    #传入(driver,超时时间,函数)
    return WebDriverWait(driver,times).until(func)

ele_input=get_ele_times(driver,10,lambda driver: driver.find_element_by_id('kw'))
ele_input.send_keys('python')

driver.find_element_by_id('su').click()

driver.implicitly_wait(10)    #此方法较实用,发现元素立即返回,没有则一直等,直到10秒时间到,超时
ele2=driver.find_element_by_partial_link_text('百度百科')
ele2.click()

print(driver.title)

driver.switch_to_window(driver.window_handles[-1])    #切换窗口
time.sleep(1)
print(driver.title)   #标题成功更换

driver.find_element_by_css_selector('body > div.navbar-wrapper > div > div > div > div > div > dl.index > dt > a').click()

time.sleep(3)
driver.back()     #返回上一页
driver.close()    #关闭当前页

driver.switch_to_window(driver.window_handles[-1])   #切换窗口句柄
print(driver.title)   #标题切换成功

driver.execute_script("window.scrollBy(0,700)","")  #向下滚动指定元素
driver.find_element_by_partial_link_text('廖雪峰的官方网站').click()
print(driver.title)
time.sleep(3)
driver.quit()  #退出浏览器
print('完成')

