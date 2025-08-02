import cv2 as cv

def nothing(x):
    print(x)
 
cv.namedWindow("TRACKBAR")

cv.createTrackbar("CP","TRACKBAR",10,400,nothing)

switch="color/gray"
cv.createTrackbar(switch,"TRACKBAR",0,1,nothing)

while(1):
    pic=cv.imread("./photos/dog.jpg")
    
    curr_pos=cv.getTrackbarPos("CP","TRACKBAR")
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(pic,str(curr_pos),(20,100),font,2,(0,0,255),3,cv.LINE_AA)
     
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    
    sw=cv.getTrackbarPos(switch,"TRACKBAR")

    if sw==0:
        pic[:]=0
    else:
        pic=cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
    cv.imshow("TRACKBAR",pic)
  
cv.destroyAllWindows()