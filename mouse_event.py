import cv2 as cv
import numpy as np
'''
events=[i for i in dir(cv) if 'EVENT' in i]    #to see all mouse events
print(events)
'''
def clickEvent(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv.circle(img,(x,y),3,(255,0,0),-1)
        blank=np.zeros((512,512,3),np.uint8)
        blank[:]=[blue,green,red] #to fill every point or pixel with the color of the point clicked on the original img
        cv.imshow("Colored Img",blank)

img=cv.imread("./photos/LZS.jpg")
cv.imshow("image",img)
cv.setMouseCallback("image",clickEvent)
cv.waitKey(0)
cv.destroyAllWindows()
