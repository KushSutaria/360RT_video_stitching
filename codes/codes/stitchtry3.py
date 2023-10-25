#!/usr/bin/env python

'''
Stitching sample
================
Show how to use Stitcher API from python in a simple way to stitch panoramas
or scans.
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

import time
import argparse
import sys
import os
from os.path import isfile, join
from multiprocessing import Process
from multiprocessing import Pool


modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)

parser = argparse.ArgumentParser(prog='stitching.py', description='Stitching sample.')
parser.add_argument('--mode',
type = int, choices = modes, default = cv.Stitcher_PANORAMA,
help = 'Determines configuration of stitcher. The default is `PANORAMA` (%d), '
'mode suitable for creating photo panoramas. Option `SCANS` (%d) is suitable '
'for stitching materials under affine transformation, such as scans.' % modes)
parser.add_argument('output', default = 'result.jpg',
help = 'Resulting image. The default is `result.jpg`.')
parser.add_argument('img', nargs='+', help = 'input images')

__doc__ += '\n' + parser.format_help()

def split_name(a):
	l=[]
	a=a.replace(".png","")
	b=a.split("-")
	c=b[0].split(",")
	q=0
	for q in range(len(c)):
		l.append(c[q])
		q+=1
	l.append(b[1])	
	return l

def time_compare(a,b):
	if(a[0]>b[0]):	#for hours
		return a
	elif(a[0]==b[0]):
		if(a[1]>b[1]): #for minutes
			return a
		elif(a[1]==b[1]):
			if(a[2]>b[2]): #for seconds
				return a
			elif(a[2]==b[2]):
				if(a[3]>b[3]):
					return a
				else:	
					return b
			else:
				return b
		else:
			return b
	else:
		return b

def stitchs(l):
	stitcher = cv.Stitcher.create(0)
	status, pano = stitcher.stitch(l[0])
	#imgs=[]
	cv.imwrite(".//stitched1//stitch"+str(l[1])+".jpg", pano)
	###print(status)
	if(status > 0):
		os.remove(".//stitched1//stitch"+str(l[1])+".jpg")
		
	print('Done',l[1])
#def resize():	
    
def main():
	
	#args = parser.parse_args()
	pathIn1= './/f11//'
	pathIn2= './/f22//'
	# read input images
	imgs1 = []
	imgs2 = []
	imgs3 = []
	imgs4 = []
	files1 = [f for f in os.listdir(pathIn1) if isfile(join(pathIn1, f))]#for sorting the file names properly
	files2 = [f for f in os.listdir(pathIn2) if isfile(join(pathIn2, f))]#for sorting the file names properly
	###print(files1)
	###print(files2)
	d1=split_name(files1[0])
	d2=split_name(files2[0])
	print(d1,d2)
	w=time_compare(d1,d2)
	print(w)
	i=0
	if(w==d1):
		while(i!=len(files2)):
			print(files2[i],i)
			d=split_name(files2[i])
			w1=time_compare(w,d)
			print(w,d,w1)
			if(w1==w):
				files2.pop(i)
				i-=1
			else:
				break
			i+=1
	else:
		while(i!=len(files1)):
			print(files1[i])
			d=split_name(files1[i])
			w1=time_compare(w,d)
			print(w,d,w1)
			if(w1==w):	
				files1.pop(i)
				i-=1
			else:
				break
			i+=1
	###print(files1[0])
	###print(files2[0])
	###print(files1)
	###print(files2)
		
	p=0
	if(len(files1)>len(files2)):
		p=len(files2)
	else:
		p=len(files1)
	i=0	
	while(i!=((len(files2)) if len(files2) < len(files1) else (len(files1)))):
		f=split_name(files1[i])
		g=split_name(files2[i])
		print(i,f,g)
		if(f[0]==g[0] and f[1]==g[1] and f[2]==g[2]):
			i+=1
			continue
		else:
			if(f[0]==g[0] and f[1]==g[1] and f[2]>g[2]):
				u=i
				j=u
				while(j!=len(files2)):
					k=split_name(files2[j])
					if(k[0]==g[0] and k[1]==g[1] and k[2]==g[2]):
						print("files2deleted",k)
						files2.pop(j)
						j-=1
					elif(k[0]==g[0] and k[1]==g[1] and k[2]==f[2]):
						print("bachigyo",k)
						break
					j+=1	
				i-=1	
			elif(f[0]==g[0] and f[1]==g[1] and f[2]<g[2]):
				u=i
				j=u
				while(j!=len(files2)):
					k=split_name(files1[j])
					if(k[0]==g[0] and k[1]==g[1] and k[2]==f[2]):
						print("files1deleted")
						files1.pop(j)
						j-=1
					elif(k[0]==g[0] and k[1]==g[1] and k[2]==g[2]):
						break
					j+=1	
				i-=1
		i+=1
	if(len(files1)>len(files2)):
		p=len(files2)
	else:
		p=len(files1)
		
	for i in range(p):
		filename1 = pathIn1 + files1[i]
		filename2 = pathIn2 + files2[i]	

		img = cv.imread(filename1)
		img1 = cv.imread(filename2)
		imgs1.append(img)
		imgs2.append(img1)

	proc = []
	start_time = time.perf_counter()
	r=[]
	for i in range(p):
		#res =[]
		l=[]
		imgs = []
		imgs.append(imgs1[i])
		imgs.append(imgs2[i])
		l.append(imgs)
		l.append(i)
		r.append(l)
	with Pool(6) as p:
		p.map(stitchs, r)
	print(" time taken : %.4s seconds" %(time.perf_counter()-start_time))  
    #proc1 = Process(target=stitchs, args=l)
    #proc.append(proc1)
	#for i in range(p-int(p/2),p):
#		proc[i].start()
#	for i in range(p-int(p/2),p):
#		proc[i].join()

	'''
	stitcher = cv.Stitcher.create(0)
	status, pano = stitcher.stitch(imgs)
	imgs=[]
	cv.imwrite(".//stitched1//stitch"+str(i)+".jpg", pano)
	#print("hieee logs")
	#print(pano)
	#cv.waitKey(0)
	#cv.destroyAllWindows()
	print(status)
	if(status > 0):
		os.remove(".//stitched1//stitch"+str(i)+".jpg")
		continue
	print('Done')
	'''
	pathIn= './/stitched1//'
	pathOut = 'videodemo.avi'
	fps =  5
	#frame_array = []
	files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
	#print(files2)
	files3=[]
	frame_array = []
	#res_array=[]
	for i in range(len(files2)):
		files2[i]=files2[i].replace('.jpg','')
		files2[i] = files2[i].replace('stitch', '')
		files3.append(int(files2[i]))	
	#print(files3)
	files3.sort()
	#print(files3)
	#files2 = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]#for sorting the file names properly
	#files2.sort(key = lambda x: x[5:-4])
	#files2.sort()
	for i in range(len(files2)):
		filename=pathIn + 'stitch'+str(files3[i]) +'.jpg'
		#reading each files
		img = cv.imread(filename)
		#print(filename)
		#print(img)
		#if(img):
		height, width, layers = img.shape
		size = (width,height)
		#print(img.shape)
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
	'''
	pathIn= './/stitched1//'
	pathOut = 'videoaaaa.avi'
	fps =  5
	#frame_array = []
	files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
	###print(files2)
	files3=[]
	frame_array = []
	for i in range(len(files2)):
		files2[i]=files2[i].replace('.jpg','')
		files2[i] = files2[i].replace('stitch', '')
		files3.append(int(files2[i]))
	###print(files3)
	files3.sort()
	###print(files3)
	#files2 = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]#for sorting the file names properly
	#files2.sort(key = lambda x: x[5:-4])
	#files2.sort()
	for i in range(len(files2)):
		filename=pathIn + 'stitch'+str(files3[i]) +'.jpg'
		#reading each files
		img = cv.imread(filename)
		###print(filename)
		###print(img)
		#if(img):
		height, width, layers = img.shape
		size = (width,height)
		###print(img.shape)
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
    '''	
	
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
