import cv2 as cv

img=cv.imread("./photos/LZS.jpg")
cv.imshow("DOG",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#SIMPLE THRESHOLDING

threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)    #>threshold=100-->white(255),<255-->threshold=blavk(0)
cv.imshow("Simple Threshold",thresh)

threshold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)  
cv.imshow("Simple Threshold Inverse",thresh_inv)

#ADAPTIVE THRESHOLDING

adap_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)  #2-->subtracted from mean for the fine tuning of the threshold value
cv.imshow("Adaptive Threshold MEAN",adap_thresh)

adap_thresh_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,9,3)  
cv.imshow("Adaptive Threshold MEAN Inverse",adap_thresh_inv)


adap_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)  #2-->subtracted from mean for the fine tuning of the threshold value
cv.imshow("Adaptive Threshold GAUSSIAN",adap_thresh)

cv.waitKey(0)