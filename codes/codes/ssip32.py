import cv2
import os
from datetime import datetime
cam = cv2.VideoCapture(2)
	
cv2.namedWindow("test")

img_counter = 1
a=5
while True:
	ret, frame = cam.read()
	t=frame
	cv2.imshow("test", frame)
	if not ret:
		break
	k = cv2.waitKey(1)

	if k%256 == 27:
	# ESC pressed
		print("Escape hit, closing...")
		break
	img_name = r"C:/yashpd16/stitching11/stitching/frames02/"+str(img_counter)+".png"
	img_name1 = r"C:/yashpd16/stitching11/stitching/frames2/"
	cv2.imwrite(img_name, frame)
	
	#grayImage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
	#cv2.imwrite(r'C:/yashpd16/venv/Black white image.jpg', blackAndWhiteImage)
	#cv2.imwrite(r'C:/yashpd16/venv/Original image.jpg',frame)
	#cv2.imwrite(r'C:/yashpd16/venv/Gray image.jpg', grayImage)
	
	
	#print("{} written!".format(img_name))
	b=str(datetime.now()).split(" ")
	p=str(b[1])
	w=p.split(".")
	img_name1+=	str(w[0].replace(":",","))+","+str(w[1])+"-"+str(img_counter)+".png"
	print(img_name1)
	
	cv2.imwrite(img_name1, frame)
	img_counter += 1

cam.release()

cv2.destroyAllWindows()