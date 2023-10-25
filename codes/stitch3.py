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
    
def main():
    #args = parser.parse_args()
    pathIn1= './/WebCamImage1//'
    pathIn2= './/WebCamImage2//'
    # read input images
    imgs = []
    imgs1=[]
    imgs2=[]
    list1=[]
    list2=[]
    i=0
    files = [f for f in os.listdir(pathIn1) if isfile(join(pathIn1, f))]#for sorting the file names properly
    files1 = [f for f in os.listdir(pathIn2) if isfile(join(pathIn2, f))]#for sorting the file names properly
		
    p=len(files1)
    for i in range(p):
        filename = pathIn1 + files[i]
        filename1 = pathIn2 + files1[i]
        print(filename)
        print(filename1)
        #reading each files
        img = cv.imread(filename)
        img1 = cv.imread(filename1)
        #img = cv.imread(cv.samples.findFile(imgs1[i]))
        imgs.append(img)
        imgs.append(img1)
        #print(imgs)
        res =[]
        stitcher = cv.Stitcher.create(0)
        status, pano = stitcher.stitch(imgs)
        imgs=[]
        cv.imwrite(".//stitched//stitch"+str(i)+".jpg", pano)
        #print("hieee logs")
        #print(pano)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        print(status)
        if(status > 0):
            os.remove(".//stitched//stitch"+str(i)+".jpg")
            continue
        print('Done')
    pathIn= './/stitched//'
    pathOut = 'video.avi'
    fps =  18
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
