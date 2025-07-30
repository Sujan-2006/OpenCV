import cv2 as cv
import numpy as np
'''
events=[i for i in dir(cv) if 'EVENT' in i]    #to see all mouse events
print(events)
'''
def clickEvent(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(255,0,0),-1)
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(0,0,255),2)
       
        cv.imshow("image",img)

img=cv.imread("./photos/LZS.jpg")
cv.imshow("image",img)
points=[]
cv.setMouseCallback("image",clickEvent)
cv.waitKey(0)
cv.destroyAllWindows()
