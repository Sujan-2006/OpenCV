import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("./photos/LZS.jpg")
cv.imshow("LZS",img)

blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),200,255,-1)

mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("Mask",mask)

#HISTOGRAM
hist=cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title("HISTOGRAM")
plt.xlabel("Bins")
plt.ylabel("no of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
 

cv.waitKey(0)
