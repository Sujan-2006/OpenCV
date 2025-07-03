import cv2 as cv
import numpy as np

#BASIC IMAGE PROCESSIG FUNCTIONS

img=cv.imread("./photos/Luffy.jpg")

cv.imshow("Original_Luffy",img)

# convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#convert to blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

#convert to canny edges
canny=cv.Canny(blur,125,175)

#diaalating of images
dilated_img=cv.dilate(canny,(7,7),iterations=3)

#eroding of images
eroded_img=cv.erode(dilated_img,(7,7),iterations=3)

#resize the image
resized_img=cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)

#to crop the image
cropped_img=img[50:200,200:400]

cv.imshow("Functioned_Luffy",cropped_img)

#IMAGE TRANSFORMATIONS

image=cv.imread("./photos/dog.jpg")

cv.imshow("Original_Dog",image)

#image transformation

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])       #-x-->left
    dimensions=(img.shape[1],img.shape[0])            #-y-->up
    return cv.warpAffine(img,transMat,dimensions)     #x-->right
translated=translate(image,-100,-100)             #y-->down

#rotate the image

def rotate(img,angle,rotPoint=None):
    (h,w)=img.shape[:2]
    if rotPoint==None:
        rotPoint=(w//2,h//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(w,h)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(image,60)   #put - for clockwiese rotatation
rotated2=rotate(rotated,-45)

#flipping the image

Flip=cv.flip(image,0)   #1-->Horizontal flip,0-->vertical flip,-1-->both horizontal and vertical flip

cv.imshow("Transformed_Dog",Flip)

cv.waitKey(0)