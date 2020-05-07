#################################
## Image Processing using Python
#################################

#Flipping the image task

from PIL import image

#open the sample image 
img=Image.open('sample.jpeg')

#Transposing (Rows becomes Cols and Cols become Rows
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#Save it to a human seable format
transposed_img.save('corrected.jpeg')

print('Done Flipping')

#Image Enhancement using adaptive Histogram adaptation CLAHE
import cv2

#Read the image
img.cv2.imread('sample.jpeg')

#Preparation for CLAHE
clahe=cv2.createCLAHE()

#Convert to grey scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply enhancement
enh_img=clahe.apply(gray_img)	

#Save it to a file
cv2.imwrite('enhanced.jpeg',enh_img)

print('Done Enhancing')

