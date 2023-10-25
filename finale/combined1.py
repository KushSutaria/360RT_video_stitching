
#!/usr/bin/env python

'''
Stitching sample
================
Show how to use Stitcher API from python in a simple way to stitch panoramas
or scans.
'''

# Python 2/3 compatibility
#import fish_eye
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

def fisheye_func(pano,n):
    cv.namedWindow("test")
    cv.moveWindow("test",600,600)
    cv.resizeWindow("test",900,500)
    k4 = cv.waitKey(2000)
    K = np.array([[1.34480182e+03, 0.00000000e+00, 6.75693900e+02],
                  [0.00000000e+00, 1.21415726e+03, 3.82264359e+02],
                  [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    # Define distortion coefficients d
    d = np.array([ 0.10849886, -1.7438515, -0.00891307, 0.00700695, 2.84127126])
    # Read an example image and acquire its size
    h, w = pano.shape[:2]

    # Generate new camera matrix from parameters
    newcameramatrix, roi = cv.getOptimalNewCameraMatrix(K, d, (w,h), 0)

    # Generate look-up tables for remapping the camera image
    mapx, mapy = cv.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

    # Remap the original image to a new image
    newimg = cv.remap(pano, mapx, mapy, cv.INTER_LINEAR)

    # Display old and new image
    #fig, (oldimg_ax, newimg_ax) = plt.subplots(1, 2)
    #oldimg_ax.imshow(img)
    #oldimg_ax.set_title('Original image')
    #newimg_ax.imshow(newimg)
    if(n==0):
            cv.imshow("test", newimg)
    #cv2.imwrite(img_name_out,newimg)
    #newimg_ax.set_title('Unwarped image')
    #plt.show()
    cv.waitKey(500)
    cv.destroyAllWindows()
    return newimg

def main():
    cam1 = cv.VideoCapture(2)
    cam2 = cv.VideoCapture(0)   
    cv.namedWindow("test1")
    cv.namedWindow("test5")
    cv.moveWindow("test1",20,20)
    cv.resizeWindow("test1",600,500)
    cv.namedWindow("test2")
    cv.moveWindow("test2",600,20)
    cv.resizeWindow("test2",600,500)
    img_counter1 = 1
    img_counter2 = 1
    a=5
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    cv.imshow("test1", frame1)
    cv.imshow("test2", frame2)
    img_name1 = r"/home/pi/Desktop/hackathon/test/test1.jpg"    
    img_name2 = r"/home/pi/Desktop/hackathon/test/test2.jpg"    
    k1 = cv.waitKey(1000)
    k2 = cv.waitKey(1000)   
    cv.imwrite(img_name1,frame1)
    cv.imwrite(img_name2,frame2)    
    cam1.release()
    cam2.release()
    imgs=[]
    imgs.append(frame1)
    imgs.append(frame2)
    #print(imgs)
    res =[]
    stitcher = cv.Stitcher.create(0)
    status, pano = stitcher.stitch(imgs)
    cv.moveWindow("test5",600,20)
    cv.resizeWindow("test5",900,500)
    
    imgs=[]
    img_name3 = r"/home/pi/Desktop/hackathon/test/pano.jpg" 
    img_name4 = r"/home/pi/Desktop/hackathon/test/fish.jpg" 
    
    #print("hieee logs")
    #print(pano)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    print(status)
    if(status==1):
            cv.imwrite(img_name4,fisheye_func(pano),1)
        else:
            cv.imshow("test5")
            k3 = cv.waitKey(2000)
            cv.imwrite(img_name3,pano)  
            cv.imwrite(img_name4,fisheye_func(pano),0)
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

