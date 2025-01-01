# import the library
import os
import cv2
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode


source = 'race_car.mp4'
cap = cv2.VideoCapture(source)
# if not cap.isOpened():
#     print('Error')

# ret,frame = cap.read()

# plt.imshow(frame[:,:,::-1])


# viedo = YouTubeVideo('RwxVEjv78LQ',width=700,height=438)
# display(viedo)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size= (frame_width,frame_height)
out_avi = cv2.VideoWriter('race_car_out.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,size)
out_mp4 = cv2.VideoWriter('race_car_out.mp4',cv2.VideoWriter_fourcc(*'XVID'),10,size)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out_avi.write(frame)
        out_mp4.write(frame)
    else:
        break
cap.release()
out_avi.release()
out_mp4.release()
