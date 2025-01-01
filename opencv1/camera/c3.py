import cv2
import sys 
import numpy

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3 

feature_params = {
    'maxCorners': 500,
    'qualityLevel': 0.2,
    'minDistance': 15,
    'blockSize': 9
}

s=0
if len(sys.argv)>1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = 'Camera Filtrts'
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)

result = None 

source = cv2.VideoCapture(s)

while alive:
    has_frame , frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame,1) 

 #Obraca klatkę w poziomie (lustrzane odbicie) za pomocą funkcji cv2.flip. Wartość 1 oznacza lustrzane odbicie w poziomie.

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame,145,150)
    elif image_filter == BLUR:
        result =- cv2.blur(frame,(13,13))
    elif image_filter == FEATURES:
        result = frame 
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray_frame,**feature_params)
        if corners is not None:
            for x , y in numpy.int32(corners).reshape(-1,2):
                cv2.circle(result,(x,y),10,(0,255,0),1)
    cv2.imshow(win_name,result)

    key = cv2.waitKey(1)

    if key ==ord('Q') or key ==ord('q') or key ==27:
        alive = False
    elif key==ord('C') or key==ord('c'):
        image_filter = CANNY
    elif key == ord('B') or key ==ord('b'):
        image_filter = BLUR
    elif key == ord('F') or key ==ord('f'):
        image_filter = FEATURES
    elif key == ord('p') or key ==ord('p'):
        image_filter = PREVIEW
    
source.release()
cv2.destroyWindow(win_name)
