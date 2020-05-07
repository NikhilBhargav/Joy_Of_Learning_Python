# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:59:48 2020
Code to traverse a matrix in spiral fashion
@author: Nikhil Bhargava
"""

import turtle

turtle.bgcolor("white")
seurat=turtle.Turtle()

#For plotting of dots on screen
width=15
height=17
dot_distance=40   
turtle.done()

seurat.setpos(250, 250)

def spiral(m,n):
    #set color of turtle as white
    seurat.color("red")
    #starting index of row and col resp.
    k=0
    l=0
    seurat.forward(dot_distance)
     
    flag=0
    while(k<n and l<n):
        
        if(flag==1):
            seurat.right(90)
            
        # printing the 1st row from remaining row
        for i in range(l,n):
            #print(A[k][i],end=" ")
            seurat.forward(dot_distance)
            
        # Move to next row and set flag to done
        k=k+1
        flag=1
        
        #Turn turtel to right
        seurat.right(90)
        
        #Print the lst col from relamining col
        for i in range(k,m):
            #print(A[i][n-1],end=" ")
            seurat.forward(dot_distance)
            
        # Move to the second last col
        n=n-1
        #turn turtle to right
        seurat.right(90)
        
        if(k<m):
            #Printing the last row from remaining rows
            for i in range ((n-1),(l-1),-1):
                #print(A[n-1][i],end=" ")
                seurat.forward(dot_distance)
       
            m=m-1
            
        #turn turtle to right
        seurat.right(90)
        
        if(l<n):
            #printing the first col from remaining col
            for i in range(m-1,k-1,-1):
                #print(A[i][l],end=" ")
                seurat.forward(dot_distance)
            l=l+1    

#Test Code
m=20
n=20
spiral(m,n)
turtle.done()
    

