'''
Created on 03-May-2019

@author: priyanka.gupta
'''

#Import webdriver module from selenium package
from selenium import webdriver

#Path of chrome driver for windows 
chrome_driver_path = "D:\SeleniumProjects\TeachMeSelenium\chromedriver.exe"
#For Mac please comment the above line and uncomment the below line
#chrome_driver_path = "/usr/local/bin/chromedriver"

#Create object of Chrome
driver=webdriver(chrome_driver_path)
#Navigate browser to practice.teachmeselenium.com
driver.get("http://practice.teachmeselenium.com")
#Type iPhone 7 in the search box
driver.find_element_by_name("s").send_keys("iPhone 7")
#Click on Search button
driver.find_element_by_class_name("bgs-search-submit").click()
#In the next page capture price of the product
price = driver.find_element_by_class_name("price").text
print("Price of the product is " + price)
#Click on Add to Cart button
driver.find_element_by_name("add-to-cart").click();
#Click on View cart button
driver.find_element_by_link_text("View cart").click();
#Quit driver and close browser
driver.quit()