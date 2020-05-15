# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:58:21 2020

@author: Nikhil Bhargava

Collatz Conjecture
"""
def Checknum(num):
    iterations=0
    n=num
    while(num!=1):
        if(num%2==0):#Even
            num=(int)(num/2)
            iterations+=1
        else:
            num=(3*num)+1
            iterations+=1
            
    print("For",n,"it takes",iterations,"iterations to become 1")

#Test Code
Checknum(26)            

