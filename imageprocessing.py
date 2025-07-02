import cv2
img=cv2.imread("./photos/dog.jpg")
resized=cv2.resize(img,(100,200))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
croped=img[10:500,20:100]
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.line(img, (0, 0), (200, 200), (0, 255, 0), 3)
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 2)
cv2.circle(img, (100, 100), 40, (0, 0, 255), -1) 
cv2.putText(img,"I am a cute Puppy",(10,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

def rescaleFrame(frame,scale=0.5):
    w=int(frame.shape[1]*scale)
    h=int(frame.shape[0]*scale)
    dimensions=(w,h)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

resized_img=rescaleFrame(img)

cv2.imshow("dog",img)
cv2.imshow("DOG",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
