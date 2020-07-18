#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:43:01 2020

@author: nikhil1.bhargava
"""

import random

#Initialize Door and Goat Door to 0
doors=[0]*3
goatDoor=[0]*2

#No. of wins by Swaping 
swap=0
#No. of wins by not Swaping 
noSwap=0

#Door having Car behind it. There are total of 3 doors 
doorCar=random.randint(0,2)

doors[doorCar]="Car"
for i in range (0,3):
    if(i==doorCar):
        continue
    else:
        doors[i]="Goat"
        goatDoor.append(i)

#We play 10 times
noAttempt=5
j=0

while(j<noAttempt):        
    #Let user choose one of 3 door
    choice=int(input("Enter your choice of door from 1,2 and 3 "))
    
    #Anchor opens one of the two doors having goat 
    doorOpen=random.choice(goatDoor)
    
    #Don't open same dor that user choses
    while(doorOpen==choice):
        doorOpen=random.choice(goatDoor)
    
    ch=input("Do you want to swap (say yes or no)?")
    
    #User chooses to swap
    if(ch=="yes"):
        if(doors[choice-1]=="Goat"): #he wins
            print("You Win")
            swap+=1
        else:
            print("You loose")
    #User chooses not to swap
    else:         
        if(doors[choice-1]=="Goat"): #he wins
            print("You loose")
        else:
            print("You Win")
            noSwap+=1
    j+=1
        
print("No. of Wins by Swap",swap)
print("No. of Wins by not Swapping",noSwap)