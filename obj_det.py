import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

capture=cv.VideoCapture(0)

cv.namedWindow("TRACKING")
cv.createTrackbar("LowHue", "TRACKING", 0, 255, nothing)
cv.createTrackbar("LowSat", "TRACKING", 0, 255, nothing)
cv.createTrackbar("LowVal", "TRACKING", 0, 255, nothing)
cv.createTrackbar("UpHue", "TRACKING", 255, 255, nothing)
cv.createTrackbar("UpSat", "TRACKING", 255, 255, nothing)
cv.createTrackbar("UpVal", "TRACKING", 255, 255, nothing)

while(1):
    #img=cv.imread("./photos/balls.jpg") 
    _,frame=capture.read()

    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    LH=cv.getTrackbarPos("LowHue","TRACKING")
    LS=cv.getTrackbarPos("LowSat","TRACKING")
    LV=cv.getTrackbarPos("LowVal","TRACKING")
    UH=cv.getTrackbarPos("UpHue","TRACKING")
    US=cv.getTrackbarPos("UpSat","TRACKING")
    UV=cv.getTrackbarPos("UpVal","TRACKING")

    lb=np.array([LH,LS,LV])           #blue  110,50,50
    ub=np.array([UH,US,UV])           #blue  130,255,255

    mask=cv.inRange(hsv,lb,ub)
    output=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("Tracking",frame)
    cv.imshow("Mask",mask)
    cv.imshow("RESULT",output)

    if cv.waitKey(1) & 0xFF==ord("a"):
        break
capture.release()
cv.destroyAllWindows()
  