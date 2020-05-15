# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:47:44 2020

@author: Nikhil Bhargava
Whatsapp automation using Python using Selenium
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome("chromedriver")
browser.get("https://web.whatsapp.com/")
wait=WebDriverWait(browser,600)

#Send bulk messages to yur friend
target='"XXX"'
msg="Hello"

x_arg='//span[contains(@title,' + target + ')]'

fdtitle=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)) )

print(fdtitle)
print("Wait for some time")

#Sleep for 4 seconds to load all contacts
time.sleep(4)


fdtitle.click()

message = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

message.send_keys(msg)
sendbutton = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()
browser.close()