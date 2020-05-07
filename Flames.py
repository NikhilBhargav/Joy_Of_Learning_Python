########################################
## Python implementation of FLAMES game
########################################
import string
'''
 Function to define removal of common 
 letters from both strings
'''
def removeMatchLetter(l1, l2):
	for i in range(len(l1):
		for j in range(len(l2):
			#Match found
			if(l1[i]==l2[j]:
				common=l1[i]
				#Remove common elem from both list
				l1.remove(common)
				l2.remove(common)
				#Create new list
				lnew=l1+['*']+l2
				return ([lnew, True])	
	
	#No match found
	lnew=l1+['*']+l2
	return ([lnew, False])
	
	
	
	
#Take names, convert to lowercase and trim whitespaces
firstName=input("Enter first person's name")
firstName=firstName.lower()
firstName=firstName.replace(" ","")

secondName=input("Enter second person's name")
secondName=secondName.lower()
secondName=secondName..replace(" ","")

list1=list(firstName)
list2=list(secondName)
continue=True

while continue==True:
	returnList=removeMatchLetter(list1, list2)
	conList=returnList[0]
	continue=returnList[1]
	start_index=conList.index('*')
	#Use slicing around * to get L1 and L2
	l1=conList[:start_index]
	l2=conList[start_index+1:]

#Get final count of unique letters in both lists
count=len(l1)+len(l2)
grid=['Friends','Love','Affection','Marriage','Enemy','Sibling']

#Where to split
split_index=(count%len(grid))-1
if(split_index>=0):
	right=grid[split_index+1:]
	left=grid[:split_index]
	grid=right+left
else: #Split index points to last element
	grid=grid[:len(grid)-1]

print("FLAMES result for ",firstName,"and",secondName,"is",*grid,end="")

	
	