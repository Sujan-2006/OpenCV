import cv2 as cv

dog=cv.imread("./photos/dog.jpg")
cv.imshow("DOG",dog)

#Average Blur
average=cv.blur(dog,(5,5))
cv.imshow("Average Blur", average)

#Gaussian Blur
gauss=cv.GaussianBlur(dog,(5,5),0)
cv.imshow("Gaussian Blur", gauss)

#median blur
median=cv.medianBlur(dog,5)
cv.imshow("Median Blur", median)

#bilateral blur
bilateral=cv.bilateralFilter(dog,5,20,35)
cv.imshow("Bilateral Blur",bilateral)

cv.waitKey(0)