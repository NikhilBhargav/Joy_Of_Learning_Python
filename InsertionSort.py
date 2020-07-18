#InsertionSort
def InsertionSort(list):
    for slicelast in range(len(list)):
        pos=slicelast
        while ((pos>0) &(list[pos]<list[pos-1])):
            (list[pos],list[pos-1])=(list[pos-1],list[pos])
            pos=pos-1
    print ("InsertionSort over")

#test code
list=[34,45,12,3,67,91,100]
print ("Original list=", list)
InsertionSort(list)
print ("Sorted list=", list)
