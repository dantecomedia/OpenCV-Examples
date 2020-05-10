import cv2

cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("demo.mp4", fourcc, 20.0,(640,480))
print(cap.isOpened())
while(True):
	ret,frame=cap.read()
	if ret == True:
		gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		out.write(gray)
		cv2.imshow("frame", gray)
		#cv2.imshow("frame", frame)
		#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		

		if cv2.waitKey(1) & 0XFF == ord('q'):
			break
	else:
		break


cap.release()
out.release()
cv2.destroyAllWindows()