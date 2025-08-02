import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
blank=np.zeros((500,500,3),dtype='uint8')
cv.namedWindow("TRACKBAR")

cv.createTrackbar("B","TRACKBAR",0,255,nothing)
cv.createTrackbar("G","TRACKBAR",0,255,nothing)
cv.createTrackbar("R","TRACKBAR",0,255,nothing)

switch="0:OFF\n1:ON"
cv.createTrackbar(switch,"TRACKBAR",0,1,nothing)

while(1):
    cv.imshow("TRACKBAR",blank)
    k=cv.waitKey(1) & 0xFF
    if k==ord("a"):
        break
    blue=cv.getTrackbarPos("B","TRACKBAR")
    green=cv.getTrackbarPos("G","TRACKBAR")
    red=cv.getTrackbarPos("R","TRACKBAR")
    sw=cv.getTrackbarPos(switch,"TRACKBAR")

    if sw==0:
        blank[:]=0
    else:
        blank[:]=[blue,green,red]
  
cv.destroyAllWindows()