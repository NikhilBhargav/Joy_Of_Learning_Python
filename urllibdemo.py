# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:52:16 2020

@author: Nikhil Bhargava
"""

import urllib.request
try:
    url=urllib.request.urlopen("https://www.python.org")
    content=url.read()
    url.close()
except urllib.error.HTTPError:
    print("Webpage not found!!!")
    exit()
    
f=open('python.html',"wb")
f.write(content)
f.close()
