###
##Python code for Snake and Ladder Game 
###


from PIL import Image
import random


end=100

def showBoard():
    #slb.jpg is a picture of Snake and Ladded Board
	img=Image.open('slb.jpg')
	img.show()
	
def play():
    #Get Both players names
    p1Name=input("Player 1, Enter your name: ")
    p2Name=input("Player 2, Enter your name: ")	
	
	#Reset initial points for both players as 0
    pp1=0
    pp2=0
	
	#Reset turn variable
    turn=0
    while(True):
        if(turn%2==0):
            #Player 1's turn now
            print(p1Name,"your turn now ")
            #player1 wanna continue
            choice=int(input("Press 1 to continue or 0 to quit "))
            if(choice==0):
                #Player 1 wants to quit
                print(p1Name, "scored ",pp1)
                print(p2Name, "scored ",pp2)
                print("Game ends now. Thanks for playing!")
                break
            else:
                #Player 1 wanna continue so roll a dice to get 1 to 6
                dice=random.randint(1,6)
                print(p1Name," got ",dice)
                #add P1 score
                pp1+=dice
                pp1=checkLadder(pp1)
                pp1=checkSnake(pp1)
                #Check if the player goes beyond the board
                if(pp1>end):
                    pp1=end
                print(p1Name, " Your score ",pp1)
                if(reachedEnd(pp1)):
                    print(p1Name, "won")
                    break		
        else:           
            #Player 2's turn now
            print(p2Name,"your turn now ")
            #player2 wanna continue
            choice=int(input("Press 1 to continue or 0 to quit "))
            if(choice==0):
                #Player 2 wants to quit
                print(p2Name, "scored ",pp2)
                print(p1Name, "scored ",pp1)
                print("Game ends now. Thanks for playing!")
                break
            else:
                #Player 2 wanna continue so roll a dice to get 1 to 6
                dice=random.randint(1,6)
                print(p2Name," got ",dice)
                #add P1 score
                pp2+=dice
                pp2=checkLadder(pp2)
                pp2=checkSnake(pp2)
                #Check if the player goes beyond the board declare him winner
                if(pp2>end):
                    pp2=end
                print(p2Name, " Your score ",pp2)
                if(reachedEnd(pp2)):
                    print(p2Name, "won")
                    break		 
        #Increment turn to give chance to other player        
        turn+=1            
                
                
def reachedEnd(score):
    if(score==end):
        return True
    else:
        return False
            
def checkSnake(score):
    if(score==25):
        print("Snake")
        return 5
    elif (score==34):
        print("Snake")
        return 1
    elif (score==47):
        print("Snake")
        return 19
    elif (score==65):
        print("Snake")
        return 52
    elif (score==87):
        print("Snake")
        return 57
    elif (score==91):
        print("Snake")
        return 61
    elif (score==99):
        print("Snake")
        return 69
    else:
        #No Snake
        return score
    
    
def checkLadder(score):
    if(score==3):
        print("ladder")
        return 51
    elif (score==6):
        print("ladder")
        return 27
    elif (score==20):
        print("ladder")
        return 70
    elif (score==36):
        print("ladder")
        return 55
    elif (score==63):
        print("ladder")
        return 95
    elif (score==68):
        print("ladder")
        return 98
    else:
        #No ladder
        return score    
    
  
showBoard()    
play()