import cv2 as sujan
capture=sujan.VideoCapture("./videos/zoro.mp4")

#funtion for existing video
def rescaleFrame(frame,scale=0.5):
    w=int(frame.shape[1]*scale)
    h=int(frame.shape[0]*scale)
    dimensions=(w,h)
    return sujan.resize(frame,dimensions,interpolation=sujan.INTER_AREA)

'''
#live video 
def changeRes(w,h):
    capture.set(3,w)
    capture.set(4,h) 
'''

while True:
    isTrue,frame=capture.read()
    resized_frame=rescaleFrame(frame)

    sujan.imshow("ZORO",frame)
    sujan.imshow("zoro",resized_frame)
    if sujan.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
sujan.destroyAllWindows()
