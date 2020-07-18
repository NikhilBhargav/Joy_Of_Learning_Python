'''List are mutable so I can change it in place there and then on
But string is immutable and tuhs I cannot change it directly'''
#// is quotient operator E.g 4//2=2, 78//3=26

# For immutable value, assignment operator makes a fresh copy
# For mutable value, assignment doesnot make a new copy
# You can make a new list by using full slice list[:]
# x is y checks if x and y refers to the same object
# + operator works in List

# definition of function
# def function_name(arg a, arg b,..):
#    stmt1
#    ....
#    return
#
# for n in range(1,n+1)
#    stmt...
#
# for n in List
#    stmt...
#
# range(i,j,k) means increment i in steps of k till j
# list(range(0,5))=[0,1,2,3,4] list of range will give me a list
# Concatenation (using +) cretes a new list
# list_1.extend(list_2) adds all elements of list_2 to end of list_1
#
# Use slices on list with extreme caution
# if x in l means is x present in list l
# l.index(x) gives leftmost index of x in list l
#
# break allows us to jump out of a loop
#
#
#



#print ("Hello World")

def BinarySearch(list,value,left,right):
    if (right<left):
        print("Invalid list boundaries\n")
        return (-1)
    mid=int((left+right)/2)
    if(value==list[mid]):
        return (mid)
    if(value<list[mid]):
        return(BinarySearch(list,value,left,mid-1))
    else:
        return(BinarySearch(list,value,mid+1,right))

l=[2,4,7,9,13,31,45,56]
value=11
index=BinarySearch(l,value,0,len(l))
print("index=",index)
if(index!=-1):
    print(value,"is present in list at position",(index+1))
else:
    print(value,"is not present in list")



'''
def factorial(n):
    if (n<=1):
        return (1)
    else:
        return(n*factorial(n-1))
n=6
print ("Factorial of ",n,"is ",factorial (n))
'''
