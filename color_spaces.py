import cv2 as cv

img = cv.imread("./photos/dog.jpg")

cv.imshow("Original dog",img)

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

cv.waitKey(0)

