# -*- coding: utf-8 -*-
"""
Spyder Editor

Python classes for Point and Line
@author: Nikhil Bhargava
"""

import sys,math


# Class definition
class Point:
    
    def __init__(self,x=0,y=0):
        #print("Inside constructor of Point")
        self.x_cord=x
        self.y_cord=y
    
    #Destructor is automatically called at end of program
    #def __del__(self):
        #print("Inside destructor of Point")
    
    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x_cord, self.y_cord)
    
    def getPoint(self):
        print("Point is (",self.x_cord,",",self.y_cord,")")
        
    def setPoint(self,x,y):
        print("Point was (",self.x_cord,",",self.y_cord,")")
        self.x_cord,self.y_cord=x,y
        print("Point now (",self.x_cord,",",self.y_cord,")")

class Line:
    def __init__(self, p1, p2):
        self.start = Point(x1,y1)
        self.end = Point(x2,y2)
	
    def __str__(self):
        x1,y1 = self.start.x_cord,self.end.y_cord
        x2,y2 = self.end.x_cord,self.end.y_cord
        line = "((%f,%f),(%f,%f))" % (x1,y1,x2,y2)
        return line
     
    __repr__ = __str__
    
    def length(self):
        dist_x = abs(self.end.x_cord - self.start.x_cord)
        dist_y = abs(self.end.y_cord - self.start.y_cord)
        dist_x_squared = dist_x ** 2
        dist_y_squared = dist_y ** 2
        line_length = math.sqrt(dist_x_squared + dist_y_squared)
        return line_length
	
    def slope(self):
        dist_y = self.end.y_cord - self.start.y_cord
        dist_x = self.end.x_cord - self.start.x_cord
        line_slope = dist_y/dist_x
        return line_slope
        
# Main Code
print ("Creating a Line")

x1 = int(input("Enter a x1 value: "))
y1 = int(input("Enter a y1 value: "))
p1 = Point(x1,y1)
#print (p1)

x2 = int(input("Enter a x2 value: "))
y2 = int(input("Enter a y2 value: "))
p2 = Point(x2,y2)
#print (p2)

line = Line(p1,p2)

print ("What are the lines attributes?")
print ("Select one:")
print ("1. Display line")
print ("2. Display line's length")
print ("3. Display line's slope")
print ("4. Quit program")

choice=0
while choice!=4:   
    choice_string = input("Make a choice: ")
    try:
        choice = int(choice_string)
    except ValueError:
        sys.exit("Not an integer!  Goodbye!")
    
    if choice == 1:
        print (line)
    elif choice == 2:
        line_length = line.length()
        print ("Length is %f " % line_length)
    elif choice == 3:
        line_slope = line.slope()
        print ("Slope is %f " % line_slope)
    elif choice == 4:
        print ("Goodbye!")
    else:
        sys.exit("Wrong response Goodbye!")
         