# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:48:14 2020

@author: Nikhil Bhargava
Calendar using Python
"""
import calendar


def CheckLeap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False


def CheckValidDate(dt, mo, yr, leap):
    if(leap):
        if mo==2: #February
            if dt<30:
                return True
            else:
                return False
        else:
            if mo<8:
                if mo%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if mo%2==0:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False                
    else:
        if mo==2: #February
            if dt<29:
                return True
            else:
                return False
        else:
            if mo<8:
                if mo%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if mo%2==0:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False           
                               

def GetDay(day_index):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return(days[day_index])
    
'''
Main
'''
flag=True

#Takea valid year
while (flag==True):    
    year=int(input("Enter year (1978-2020): "))
    if(year<1978):
        print("Enter a valid year b/w 1978 till 2020")
        flag=True
    else:
        flag=False

flag=True
#Takea valid month
while (flag==True):    
    month=int(input("Enter month (1-12): "))
    if( (month<0) or (month>12) ):
        print("Enter a valid month b/w 1 to 12")
        flag=True
    else:
        flag=False
        
leap=CheckLeap(year)

flag=True
#Takea valid date
while (flag==True):    
    date=int(input("Enter date (1-31): "))
    if date >0 and CheckValidDate(date, month, year, leap):      
        flag=False
    else:
        flag=True

day_index=calendar.weekday(year,month,date)
day=GetDay(day_index)
print("\n")
print(date,"/",month,"/",year,"falls on", day)