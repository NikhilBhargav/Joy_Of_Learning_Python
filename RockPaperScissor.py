#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:27:43 2020

Rock, Paper Scissor game
@author: nikhil1.bhargava
"""

def rockPaperScissor(player1_choice,player2_choice,secretbit_player1,secretbit_player2):
    p1=int(player1_choice[secretbit_player1])
    p2=int(player2_choice[secretbit_player2])
    if(player1[p1]==player2[p2]):
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print("Player 1 wins")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("Player 2 wins")
    elif(player1[p1]=="Paper" and player2[p2]=="Scissor"):
        print("Player 2 wins")
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player 1 wins")    
    elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print("Player 1 wins")
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print("Player 2 wins")    
    
    
    
player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Paper',1:'Rock',2:'Scissor'}

while(True):
    player1_choice=input("Player 1, Enter your choice as 3 or more digit number ")
    player2_choice=input("Player 2, Enter your choice as 3 or more digit number ")
    
    #Secret bit position
    secretbit_player1=int(input("Player 1, Enter your secret bit position (0-2) "))
    secretbit_player2=int(input("Player 2, Enter your secret bit position (0-2) "))
    
    rockPaperScissor(player1_choice,player2_choice,secretbit_player1,secretbit_player2)
    ch=input("Do you want to continue? (y/n)")
    if(ch=='n'):
        break