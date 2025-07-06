import cv2 as cv
import numpy as np

dog=cv.imread("./photos/dog.jpg")
gray=cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#LAPLACIAN
laplacian=cv.Laplacian(gray,cv.CV_64F)
laplacian=np.uint8(np.absolute(laplacian))
cv.imshow("Laplacian",laplacian)

#SOBEL
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combinexy=cv.bitwise_or(sobelx,sobely)
cv.imshow("SOBEL X",sobelx)
cv.imshow("SOBEL Y",sobely)
cv.imshow("SOBEL Combined",combinexy)

#CANNY
canny=cv.Canny(gray,125,200)
cv.imshow("Canny",canny)

cv.waitKey(0)