#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:53:45 2020

Factorial of a number n
@author: nikhil1.bhargava
"""

def factorial(n):
    if (n==1):
        return 1
    elif (n>1):
        return ( n*factorial(n-1) )
    else:
        print("Factorial is not defined for negative numbers")

#Test Code
num=int(input("Enter the number whose factorial you want: " ))
fact=factorial(num)
if(fact!=None):
    print("Factorial of",num,"is",fact)        