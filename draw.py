import cv2 as cv
import numpy as np

blank_img= np.zeros((500,500,3),dtype='uint8')
blank_img[200:300,250:350]=0,0,255
cv.rectangle(blank_img,(0,0),(blank_img.shape[1]//2,blank_img.shape[0]//2),(255,0,255),thickness=cv.FILLED)
cv.circle(blank_img,(blank_img.shape[1]//2,blank_img.shape[0]//2),40,(0,255,255),thickness=3)
cv.line(blank_img,(40,50),(100,200),(255,255,0),thickness=3)
cv.putText(blank_img,"Hi!! I am SUJAN!",(100,300),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("BLANK IMAGE", blank_img)

cv.waitKey(0)
cv.destroyAllWindows()
