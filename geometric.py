import numpy as np 
import cv2



#Loading image using imread
img= cv2.imread("mandrill_colour.png",1)

#uncomment to load a blank tensor with the given dimension

#img=np.zeros([512,512,3], np.uint8)

#for drawing the line on the image
#first parameter is the image , second is the first co-ordinate and third is the second co-ordinate and the third is the colour of the line and last one is the line width
img=cv2.line(img,(0,245),(255,245),(0,0,255),10)
#same parameter as above and negative  of last parameter signfy the fill option
img =cv2.rectangle(img,(0,20),(60,60),(255,0,0),-1)
#for drawing the circle
img= cv2.circle(img,(90,90),63,(0,0,255),-1)

#font style
font = cv2.FONT_HERSHEY_SIMPLEX 
#for putting the text onto the image 

img=cv2.putText(img,'Rahul',(125,50), font, 1,(0,255,255), 1, cv2.LINE_AA)

# to show the image 
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()