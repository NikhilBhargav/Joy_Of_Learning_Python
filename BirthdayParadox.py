#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:53:35 2020

@author: nikhil1.bhargava
Python code for B'day paradox
"""

import random
import datetime

birthday=[]
i=0

#Sample size is N=50
while(i<50):
    #Oldest person ever lived was 122 years old
    year=random.randint(1898,2020)
    #check for leap year
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=True
    else:
        leap=False
    month=random.randint(1,12
                         )
    #Leap year's Feb has 29 days
    if(month==2 and leap==True):
        day=random.randint(1,29)
    elif(month==2 and leap==False):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 or month<7):
        day=random.randint(1,31)    
    elif(month%2!=0 or month>7 and month<12):
        day=random.randint(1,31)    
    else:
        day=random.randint(1,30)
    
    dd=datetime.date(year,month,day)
    dayOfYear=dd.timetuple().tm_yday
    i+=1
    birthday.append(dayOfYear)
    
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i+=1
