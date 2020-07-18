# Selection Sort

def SelectionSort (l):
    for start in range(len(l)):
        #assume minimum pos is start of list
        MinPos=start
        for i in range(start+1,len(l)):
            if l[i]<l[MinPos]:
                MinPos=i
        (l[start],l[MinPos])=(l[MinPos],l[start])
