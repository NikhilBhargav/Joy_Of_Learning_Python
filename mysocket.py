# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:36:26 2020

@author: Nikhil Bhargava
Simple socket program usng python
"""

import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode(),end='')

mysock.close()
