import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("./photos/LZS.jpg")
cv.imshow("LZS",img)

blank=np.zeros(img.shape[:2],dtype='uint8')

'''
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
'''
mask=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),200,255,-1)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Mask",masked)

#COLORED HISTOGRAM

plt.figure()
plt.title("HISTOGRAM")
plt.xlabel("Bins")
plt.ylabel("no of pixels")
colors=('b','g','r')
for i,clo in enumerate(colors):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])    #change mask to None to get the colored histogram of the whole image
    plt.plot(hist,color=clo)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
