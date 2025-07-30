import cv2 as cv
import numpy as np
img1= cv.imread("./photos/LZS.jpg")
img2= cv.imread("./photos/dog.jpg")
img1= cv.resize(img1, (300, 300))
img2 = cv.resize(img2, (300, 300))
img3=cv.add(img1,img2)
  
cv.imshow("Combined", img3)
cv.waitKey(0)