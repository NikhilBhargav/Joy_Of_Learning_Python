# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Nikhil Bhargava
"""

import urllib.request, urllib.error, urllib.parse

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print (line.decode().strip())