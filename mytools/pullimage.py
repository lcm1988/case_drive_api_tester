#coding:utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(2)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(u"猪")
driver.find_element_by_xpath('//*[@id="su"]').click()
sleep(10)
driver.quit()
