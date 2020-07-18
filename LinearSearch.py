#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:13:21 2020
Linear Search o(n)
@author: nikhil1.bhargava
"""


def linearSearch(NumList,num):
    nElem=len(NumList)
    for i in range(nElem):
        if (num==NumList[i]):#Match found
            print(num,"exists at position",(i+1) )
            break;        
    if(i==(nElem-1)):
        print(num,"doestnot exists in given list")    

List=[1,3,12,45,2,6,76,13]
num=46
linearSearch(List,num)