import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

def fisheye_func(K,d):
	# Define camera matrix K
	#K = np.array([[1.34480182e+03, 0.00000000e+00, 6.75693900e+02],
	#			  [0.00000000e+00, 1.21415726e+03, 3.82264359e+02],
	#			  [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

	# Define distortion coefficients d
	#d = np.array([ 0.10849886, -1.7438515, -0.00891307, 0.00700695, 2.84127126])

	pathIn= './/stitched1//'
	files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
	print(files2)
	for i in range(len(files2)):
	# Read an example image and acquire its size
		img_name_in=r"C:\yashpd16\stitching11\stitching\stitched1\stitch"+str(i)+".jpg"
		img_name_out=r"C:\yashpd16\stitching11\stitching\stitched2\stitch"+str(i)+".jpg"
		img = cv2.imread(img_name_in)
		h, w = img.shape[:2]

		# Generate new camera matrix from parameters
		newcameramatrix, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)

		# Generate look-up tables for remapping the camera image
		mapx, mapy = cv2.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

		# Remap the original image to a new image
		dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
		#x,y,q,h = roi
		#dst = dst[y:y+h, x:x+q]
		cv2.imwrite(img_name_out,dst)
		# Display old and new image
		#fig, (oldimg_ax, newimg_ax) = plt.subplots(1, 2)
		#oldimg_ax.imshow(img)
		#oldimg_ax.set_title('Original image')
		#newimg_ax.imshow(newimg)
		#cv2.imwrite(img_name_out,newimg)
		#newimg_ax.set_title('Unwarped image')
		#plt.show()