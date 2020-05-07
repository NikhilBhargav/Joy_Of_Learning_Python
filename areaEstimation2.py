###############################################
# Py method to calculate RGB value of an image
###############################################
from PIL import image
import random

im=image.open("map-o1.png")
rgb_im=im.convert("RGB")
count_India=0
count_Punjab=0
count=0

areaIndia=3287263

while(count<=1000000):
	x=random.randint(0,2480)
	y=random.randint(0,2735)
	z=0
	r,g,b=rgb_im.getpixel((x,y))
	if(r==60):
		count_India=count_India+1
		count=count+1
	else:
		if(r==80):
			count_Punjab=count_Punjab+1
			count=count+1

areaPunjab=(count_Punjab/count_India)*areaIndia
print(Estimated Area of Punjab in sq km is ",areaPunjab)