# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:39:47 2020

@author: Nikhil Bhargava
"""


import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

#Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter: ")
html=urllib.request.urlopen(url,context=ctx).read()

soup=BeautifulSoup(html,'html.parser')

#Retrieve all the anchor tags
tags=soup('a')

for tag in tags:
    print (tag.get('href',None))
