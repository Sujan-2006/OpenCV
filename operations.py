import cv2 as cv
import numpy as np
img=cv.imread("./photos/dog.jpg")
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)           
img=cv.merge((b,g,r))
cv.imshow("Dog",img)

cv.waitKey(0)