import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

# Define camera matrix K
K = np.array([[1.34480182e+03, 0.00000000e+00, 6.75693900e+02],
              [0.00000000e+00, 1.21415726e+03, 3.82264359e+02],
              [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

#K = np.array([[1.29206209e+03, 0.00000000e+00, 3.61768374e+02],
#			  [0.00000000e+00, 1.29367661e+03, 2.47701116e+02],
#              [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])			  
# Define distortion coefficients d
d = np.array([ 0.10849886, -1.7438515, -0.00891307, 0.00700695, 2.84127126])
#d = np.array([ 5.24546034e-01, -2.70787944e+01,  2.74764672e-03, -5.26315919e-03, 3.45617839e+02])
pathIn= './/stitched1//'
files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
print(files2)
# Read an example image and acquire its size
for i in range(len(files2)):
	img_name_out=r"C:\yashpd16\stitching11\stitching\stitched2\stitch"+str(i)+".jpg"
	img = cv2.imread(pathIn+files2[i])
	h, w = img.shape[:2]
	# Generate new camera matrix from parameters
	newcameramatrix, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)

	# Generate look-up tables for remapping the camera image
	mapx, mapy = cv2.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

	# Remap the original image to a new image
	newimg = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

	# Display old and new image
#	fig, (oldimg_ax, newimg_ax) = plt.subplots(1, 2)
#	oldimg_ax.imshow(img)
#	oldimg_ax.set_title('Original image')
	#newimg_ax.imshow(newimg)
	cv2.imwrite(img_name_out,newimg)
#	newimg_ax.set_title('Unwarped image')
	#plt.show()