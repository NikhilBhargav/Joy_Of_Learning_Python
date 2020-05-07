###############################################
## Python implementation for Image Compression
###############################################
'''
You are compressing a 255 bit map to 3 bit map
2^8=256  -> 2^3=8
2^5=32 times space saving 
MApping of each bit value in image will be :
0-31 will be mapped as 0
32-63 will be mapped as 1
64-95 will be mapped as 2
96-127 will be mapped as 3
128-159 will be mapped as 4
160-191 will be mapped as 5
192-223 will be mapped as 6
224-255 will be mapped as 7
'''

import numpy as np
from PIL import image

im=Image.open("kanav.jpg")
pixelMap=im.load()

#Make a new copy for kanav.jpg carrying your changes
img=Image.new(im.mode,im.size)
pixelNew=img.load()

for i in range(img.size[0]):
	for j in range(img.size[1]):
		if (pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
			pixelNew[i,j]=0
		elif (pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
			pixelNew[i,j]=1
		elif (pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
			pixelNew[i,j]=2
		elif (pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
			pixelNew[i,j]=3
		elif (pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
			pixelNew[i,j]=4
		elif (pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
			pixelNew[i,j]=5
		elif (pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
			pixelNew[i,j]=6
		elif (pixelMap[i,j]>=224 and pixelMap[i,j]<=255):
			pixelNew[i,j]=7			
 
 img.save("kanav_modified.jpg)
 
 #See the array value corresponding to kanav_modified.jpg
 j=np.asanyarray(Image.open("kanav_modified.jpg"))
 print(j)
 
 