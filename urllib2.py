# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:59:29 2020

Print counts of each word in a file from remote machine
@author: Nikhil Bhargava
"""

import urllib.request, urllib.error, urllib.parse

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts=dict()
for line in fhand:
    words=(line.decode().strip()).split(' ')
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)        
