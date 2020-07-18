#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:52:05 2020

Bubble Sort (Bad) o(n^2)
@author: nikhil1.bhargava
"""

def bubbleSort(NumList):
    nElem=len(NumList)
    if(nElem==1):
        print(Numlist[nElem])
    else:
        for i in range(nElem):
           for j in range(0,nElem-i-1):
               if(NumList[j]>NumList[j+1]):#Swap
                   temp=NumList[j]
                   NumList[j]=NumList[j+1]
                   NumList[j+1]=temp

List=[1,3,12,45,2,6,76,13]
print("List before Sorting: ",end="") 
print(*List)
bubbleSort(List)
print("List after Sorting: ",end="") 
print(*List)