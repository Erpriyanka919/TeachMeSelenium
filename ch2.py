'''
Created on 03-May-2019

@author: priyanka.gupta
'''
from selenium import webdriver
import selenium.webdriver.chrome.service as service

service=service.Service("D:\SeleniumProjects\TeachMeSelenium\chromedriver.exe")
service.start()
driver = webdriver.Chrome(service)
driver.get("http://www.teachmeselenium.com")