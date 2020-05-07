##########################
# Py Lottery simulation
##########################
import random
import matplotlib.pyplot as plt 

fee=100
prize=1000
myAccountBalance=0
numTurns=365

#X and Y Axis
x=[]
y=[]

for i in range(numTurns):
	#bet=int(input("What is your bet (1-10)"))
	bet=random.randint(1,10)
	x.append(i+1)
	
	luckyDraw=random.randint(1,10)
	y.append(myAccountBalance)
	
	#I am lucky as my bet matched
	if(bet==luckyDraw):
		myAccountBalance=myAccountBalance+prize-fee
	else:
		#No prize
		myAccountBalance=myAccountBalance-fee
	y.append(myAccountBalance)
	
print("My Account Balance after",numTurns," : ",myAccountBalance) 
plt.plot(x,y)
plt.show()
