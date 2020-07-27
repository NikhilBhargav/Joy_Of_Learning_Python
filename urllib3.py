# -*- coding: utf-8 -*-
"""
Spyder Editor

Python usage of BeautifulSoup lib

@author: Nikhil Bhargava
"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url=input("Enter: ")
html=urllib.request.urlopen(url).read()

soup=BeautifulSoup(html,'html.parser')

#Retrieve all the anchor tags
tags=soup('a')

for tag in tags:
    print (tag.get('href',None))