#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:15:44 2020

Substitution Cipher(a coded as z, b coded as a...)
@author: nikhil1.bhargava
"""

import string

dict={}
data=""

file_out=open("OutputSubsCipher.txt","w")

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]

#print(dict)    
with open("InputSubsCipher.txt") as f:
    while True:
        c=f.read(1)
        #End of file
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file_out.write(data)
        print(data)    

file_out.close()     