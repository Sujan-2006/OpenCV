import cv2 as cv
import numpy as np

img1= cv.imread("./photos/dog.jpg")
img2= cv.imread("./photos/LZS.jpg")
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
blank = np.zeros((500, 500,3), dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(50,50),(300,300),(255,0,255),-1)
circle=cv.circle(blank.copy(),(250,250),100,(255,0,255),-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

# BITWISE OPERATIONS

#AND
band=cv.bitwise_and(rectangle,circle)
cv.imshow("BAND",band)
#OR
bor=cv.bitwise_or(rectangle,circle)
cv.imshow("BOR",bor)
#NOT
bxor=cv.bitwise_xor(rectangle,circle)
cv.imshow("BXOR",bxor)
#NOT
bnot=cv.bitwise_not(rectangle)
cv.imshow("BNOT",bnot)

bxor=cv.bitwise_xor(img1,img2)
cv.imshow("IXOR",bxor)

cv.waitKey(0)