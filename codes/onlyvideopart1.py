from __future__ import print_function

import numpy as np
import cv2 as cv

import argparse
import sys
import os
from os.path import isfile, join

def main():
	pathIn= './/stitched2//'
	pathOut = 'videoafterfisheyecorrection.avi'
	fps =  5
	#frame_array = []
	files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
	print(files2)
	files3=[]
	frame_array = []
	for i in range(len(files2)):
		files2[i]=files2[i].replace('.jpg','')
		files2[i] = files2[i].replace('stitch', '')
		files3.append(int(files2[i]))
	print(files3)
	files3.sort()
	print(files3)
	#files2 = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]#for sorting the file names properly
	#files2.sort(key = lambda x: x[5:-4])
	#files2.sort()
	for i in range(len(files2)):
		filename=pathIn + 'stitch'+str(files3[i]) +'.jpg'
		#reading each files
		img = cv.imread(filename)
		print(filename)
		print(img)
		#if(img):
		height, width, layers = img.shape
		size = (width,height)
		print(img.shape)
		height = 500
		width = 900
		dim = (width, height)
		# resize image
		img = cv.resize(img, dim, interpolation = cv.INTER_AREA)  
		cv.imwrite(filename, img)
		#inserting the frames into an image array
		frame_array.append(img)
	out = cv.VideoWriter(pathOut,cv.VideoWriter_fourcc(*'DIVX'), fps, size)
	for i in range(len(frame_array)):
		# writing to a image array
		out.write(frame_array[i])
	out.release()            
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
