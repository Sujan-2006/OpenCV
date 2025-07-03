import cv2 as cv
import numpy as np

img=cv.imread("./photos/dog.jpg")
cv.imshow("Original_LZS",img)
blank_img =np.zeros(img.shape,dtype='uint8')
cv.imshow("blank", blank_img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

canny=cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

#ret,thresh=cv.threshold(gray,127,255,cv.THRESH_BINARY)
#cv.imshow("Thresh",thresh)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print("Number of contours found:", len(contours))
cv.drawContours(blank_img, contours, -1, (0, 255, 0), 1)
cv.imshow("Contours Displayed",blank_img)

cv.waitKey(0)