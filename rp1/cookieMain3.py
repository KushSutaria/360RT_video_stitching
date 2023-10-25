import P3picam
import picamera
from datetime import datetime
from subprocess import call
from time import sleep
from cookieClient3 import backup
from cookieAnalog2 import getTemp
import cv2

picPath = "/home/pi/Desktop/Ya/"
motionState = False
sleepTime = 3
#triggerTemp = 20

def captureImage(currentTime, picPath):
    # Opens the Video file
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    cap= cv2.VideoCapture('/home/pi/Desktop/Ya/Play.mp4')
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(picPath + picName,frame)
        i+=1
     
    cap.release()
    cv2.destroyAllWindows()
    


'''
def captureImage(currentTime, picPath):
    # Generate the picture's name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
'''
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

def timeStamp(currentTime, picPath, picName):
    # Variable for file path
    filepath = picPath + picName
    # Create message to stamp on picture
    message = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create command to execute
    timestampCommand = "/usr/bin/convert " + filepath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + message + "' " + filepath
    # Execute the command
    call([timestampCommand], shell=True)
    print("We have timestamped our picture.")

while True:
    currentTime = getTime()
    picName = captureImage(currentTime, picPath)
    print("Took a picture")
    completePath = picPath + picName
    print(completePath)
    backup(completePath)
    print("Everything should be backed up now.")
    break
    #motionState = P3picam.motion()
    #tempMonitor()
    #sleep(sleepTime)
    #print(motionState)
    #if motionState:
    #    currentTime = getTime()
    #    picName = captureImage(currentTime, picPath)
    #    timeStamp(currentTime, picPath, picName)
        
