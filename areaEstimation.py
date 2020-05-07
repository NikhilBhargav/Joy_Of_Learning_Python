########################################
## Area Calculation by estimation in Py 
########################################

import numpy as np
import scipy.misc
from PIL import image
import random

'''
#Image ht and width
width=5
height=4

#Image array
array=np.zeroes([height,width,3],dtype=np.uint8)	
img=Image.fromarray(array)
img.save('test.png') 
'''
scipy.misc.imread("map-01.png")
count_Punjab=0
count_India=0
count=0

areaIndia=3287263

while(count<=100000):
	#See dimension of map-01.png
	#X is taken as depth and Y is taken as length (Python is reverse)
	x=random.randint(0,2735)
	y=random.randint(0,2480)
	#map-01 is 2D
	z=0
	if(img[x][y][z]==60):#India
		count_India=count_India+1
		count=count+1
	else:
		if(img[x][y][z]==80):#Punjab
			count_Punjab=count_Punjab+1
			count=count+1
areaPunjab=(count_Punjab/count_India)*areaIndia
print("Estimated area of Punjab is :",areaPunjab," sq km")			

