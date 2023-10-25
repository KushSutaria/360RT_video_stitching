import panorama
import cv2 as cv
cv.namedWindow("test")
q=panorama.Stitcher()
a=cv.imread(".//WebCamImage1//"+"image11.jpg")
cv.imshow("test",a)
b=cv.imread(".//WebCamImage2//"+"image63.jpg")
l=[]
l.append(a)
l.append(b)
c=q.stitch(l)
#cv.imshow("test",c)