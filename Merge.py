'''
'Program to write Merge for two sorted input lists A and B
'''

def Merge(list_A, list_B):
    #Set all list indices to 0
    index_a=0
    index_b=0
    index_c=0

    # Empty new list C
    list_C=[]
    #Loop in to pick minimum of head of list A and B and put in new list C
    #Run loop till all elements of any list are added
    while (index_a<len(list_A) and index_b<len(list_B)):
        #Case 1: List_A has minimum element
        if ((list_A[index_a])<(list_B[index_b])):
                list_C.append(list_A[index_a])
                index_c=index_c+1
                index_a=index_a+1
        #Case 2: list_B contains minimum element
        else:
            list_C.append(list_B[index_b])
            index_c=index_c+1
            index_b=index_b+1

    #Case 3: List_A is Empty so copy left over slice of list_B
    if(index_a==len(list_A)):
        list_C.extend(list_B[index_b:])

    #case 4: List_B is Empty so copy left over slice of list_A
    if(index_b==len(list_B)):
        list_C.extend(list_A[index_a:])

    #return sorted list C
    return(list_C)


#Test Code
list_A=[14,23,56,78,112,201]
print ("Input List A=",list_A)

list_B=[1,14,52,89,101,174,256]
print ("Input List B=",list_B)

list_C=Merge(list_A,list_B)
print ("Sorted List C=",list_C)
