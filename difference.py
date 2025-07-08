import cv2 as cv
img1=cv.imread("./DiffIMG/i3.jpg")
img2=cv.imread("./DiffIMG/i4.jpg")
img1=cv.resize(img1,(500,500))
img2=cv.resize(img2,(500,500))
cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
blur1=cv.GaussianBlur(gray1,(5,5),1.0)
blur2=cv.GaussianBlur(gray2,(5,5),1.0)
diff=cv.absdiff(blur1,blur2)
threshold,thresh=cv.threshold(diff,100,255,cv.THRESH_BINARY_INV)
contours,hierachies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
for i in contours:
    if cv.contourArea(i)>1000:
        x,y,w,h=cv.boundingRect(i)
        cv.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)
cv.imshow("Difference",img2)
cv.waitKey(0)



