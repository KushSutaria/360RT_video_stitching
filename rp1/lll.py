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

import argparse
import sys
import os
from os.path import isfile, join

def main():
    pathIn= '/home/pi/Desktop/frames1/'
    pathOut = '/home/pi/Desktop/video.avi'
    fps =  18
    #frame_array = []
    files2  = [f for f in os.listdir(pathIn)]#for sorting the file names properly
    print(files2)
    files3=[]
    frame_array = []
    for i in range(len(files2)):
        files2[i]=files2[i].replace('.png','')
        files3.append(int(files2[i]))
    print(files3)
    files3.sort()
    print(files3)
    #files2 = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]#for sorting the file names properly
    #files2.sort(key = lambda x: x[5:-4])
    #files2.sort()
    for i in range(len(files2)):
        filename=pathIn + str(files3[i]) +'.png'
        #reading each files
        img = cv.imread(filename)
        print(filename)
        print(img)
        #if(img):
        height, width, layers = img.shape
        size = (width,height)
        print(img.shape)
        height = 480
        width = 640
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
