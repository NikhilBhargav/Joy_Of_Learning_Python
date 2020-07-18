#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:48:45 2020

Tic Tac Toe Game as Max-Min strategy 
@author: nikhil1.bhargava
"""

import numpy as np
board=np.array([ ['-','-','-'],['-','-','-'],['-','-','-'] ])
print (board)

p1='X'
p2='O'

def check_rows(symbol):
    for r in range (3):
        count=0
        for c in range(3):
            if ( board[r][c]==symbol ):
                count+=1
        if(count==3):
            #print(symbol,"won")
            return True
        
    #Not a winning move (no consecutive 3 symbol in row)    
    return (False)

    
def check_cols(symbol):    
    for c in range (3):
        count=0
        for r in range(3):
            if ( board[r][c]==symbol ):
                count+=1
        if(count==3):
            #print(symbol,"won")
            return True
        
    #Not a winning move (no consecutive 3 symbol in row)    
    return (False)
    

def check_diagonal(symbol):
    #Check both diagnols
    if (board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol ):
        #print(symbol,"won")
        return True
    if (board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol ):
        #print(symbol,"won")
        return True
    
    #Not wining move
    return (False)

def won(symbol):
    return ( check_rows(symbol) or check_cols(symbol)or check_diagonal(symbol) ) 

def place(symbol):
    print(np.matrix(board))
    while(True):
        row=int(input("Enter row (1-3) "))
        col=int(input("Enter col (1-3) "))
        #Convert row to base 0 and col also to base 0
        row=row-1
        col=col-1
        if ( (row>-1 and row<3) and (col>-1 and col<3) and board[row][col]=='-' ): 
            break
        else:
            print("Invalid input. Pls try again!")
            
    board[row][col]=symbol   
        
        
def play():
    for turn in range(9):
        #Even turm is for p1 and Odd turn is for p2
        if ( (turn%2)==0 ): #turn of p1
            print("Player 1 make your move (X)")
            place(p1)
            if won(p1):
                print("Player 1 won")
                break        
        else: #turn of p2
            print("Player 2 make your move (O)")
            place(p2)
            if won(p2):
                print("Player 2 won")
                break            
    
    #Neither player 1 nor player 2 has won so it is a draw        
    if ( not(won(p1)) and not(won(p2)) ): 
        print("Draw")
       
play()