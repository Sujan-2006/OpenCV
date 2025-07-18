import cv2 as cv
cap=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')  #('X','V','I','D')
output=cv.VideoWriter('Output_video.mp4',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        output.write(frame)
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == ord("a"):
            break
    else:
        break
cap.release() 
output.release()
cv.destroyAllWindows()
