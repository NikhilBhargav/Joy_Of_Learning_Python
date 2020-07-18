#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:05:17 2020

Binary search using recursion
@author: nikhil1.bhargava
"""

def BinarySearch(l,elem,start,end):
    #Base case is list having 1 elem
    if(start==end):
        if(l[start]==elem):
            print(start)
            return start
        else:
            return (-1)
        
    #Recursive step
    else:        
        mid=int( (start+end)/2 )
        if(l[mid]==elem):
            return(mid)
        elif(elem<l[mid]):
            #Search the left half
            return(BinarySearch(l,elem,start,mid-1))
        else:
            #search the right half
            return(BinarySearch(l,elem,mid+1,end))


#Test code
l=[1,11,34,45,23,100,56,76,12,49]
l.sort()
elem=76
index=BinarySearch(l,elem,0,len(l)-1 )
if(index==-1):
    print(elem,"is not present in",l)
else:
    print(elem,"is present at",(index+1),"in",l)