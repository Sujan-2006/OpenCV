import cv2 as cv
import numpy as np
img = cv.imread("./photos/LZS.jpg")
flower = img[350:410,400:460]  
img[343:403,170:230] = flower   
cv.imshow("Dog", img)
cv.waitKey(0)