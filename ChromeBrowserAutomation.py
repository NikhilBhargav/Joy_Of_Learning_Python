# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:40:29 2020

@author: Nikhil Bhargava
Browser automation in Python using Selenium
"""
from selenium import webdriver
browser=webdriver.Chrome("chromedriver")
browser.get("https://www.selenium.dev/")


elem=browser.find_element_by_link_text('Downloads')
elem.click()
search=browser.find_element_by_id('q')
search.send_keys('Download')

#Explore othe APIS of Selenium package
