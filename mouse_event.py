import cv2 as cv
import numpy as np
'''
events=[i for i in dir(cv) if 'EVENT' in i]    #to see all mouse events
print(events)
'''
def clickEvent(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv.FONT_HERSHEY_SIMPLEX
        text1=str(x)+','+str(y)
        cv.putText(img,text1,(x,y),font,0.5,(255,0,0),1,cv.LINE_AA)
        cv.imshow("image",img)
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv.FONT_HERSHEY_SIMPLEX
        text2=str(blue)+','+str(green)+','+str(red)
        cv.putText(img,text2,(x,y),font,0.5,(0,0,255),1,cv.LINE_AA)
        cv.imshow("image",img)

img=cv.imread("./photos/LZS.jpg")
cv.imshow("image",img)
cv.setMouseCallback("image",clickEvent)
cv.waitKey(0)
cv.destroyAllWindows()
