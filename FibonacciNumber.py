#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:39:21 2020

Program to print fibonacci numbers
@author: nikhil1.bhargava
"""

def FibonacciNumber(n):
    if(n<2):
        return n
    else:
        return (FibonacciNumber(n-1)+FibonacciNumber(n-2))

#Test Code
n=int(input("Enter a non-negative number "))
if(n<0):
    print("Fibonacci numbers are not defined for Negative numbers")
else:
    print("Fibonacci number at position",n,"is",FibonacciNumber(n))
