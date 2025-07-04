import cv2 as cv
import numpy as np

img=cv.imread("./photos/LZS.jpg")
cv.imshow("LZS",img)

blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),200,255,-1)
rectangle=cv.rectangle(blank.copy(),(50,50),(300,300),(255,0,255),-1)
#maask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+45,img.shape[0]//2+45),255,-1)

OR=cv.bitwise_or(circle,rectangle)
cv.imshow("and",OR)
masked=cv.bitwise_and(img,img,mask=OR)
cv.imshow("Masked imag",masked)

cv.waitKey(0)