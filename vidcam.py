import cv2 as cv
cap=cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
cap.set(3,700)
cap.set(4,700)
fourcc=cv.VideoWriter_fourcc(*'XVID')  #('X','V','I','D')
output=cv.VideoWriter('Output_video.mp4',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:       
        text="Width :"+str()
        cv.putText(frame,"I am SUJAN",(20,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
        output.write(frame)
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF == ord("a"):
            break
    else:
        break
cap.release() 
output.release()
cv.destroyAllWindows()
