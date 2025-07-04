import cv2 as cv
import numpy as np

img = cv.imread("./photos/dog.jpg")

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow("Original dog", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)
lab_bgr= cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB to BGR", lab_bgr)
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)

#to split the image
b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)


cv.imshow("BLUE",b)
cv.imshow("GREEN",g)
cv.imshow("RED",r)

#to print the shape of images
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#to merge the image
merged=cv.merge([b,g,r])
cv.imshow("Merged Image",merged)

cv.waitKey(0)

