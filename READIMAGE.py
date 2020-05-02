#loading opencv2
import cv2   

#loading the image
#0 = grayscale
#-1 load all channels including the alphas
#1 load image with all channels
img=cv2.imread('mandrill_modified.png',-1)
#print the image as array
print(img)
#show image with frame name image
cv2.imshow('image', img)
#load key values
#0 means don't no parameter
#values>0 destroy after given milliseconds
k=cv2.waitKey(0)
if k ==27:
	#destory all windows
	cv2.destroyAllWindows()
elif k==ord('s'):
	#is Unicode of the key is equal to the file it will save it 
	cv2.imwrite('mandrill_modified_copy_again.png', img)