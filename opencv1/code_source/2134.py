# Import libraries
import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)

image = cv2.imread('apol.jpg',cv2.IMREAD_COLOR)
#plt.imshow(image[:, :, ::-1])


# imageLine =  image.copy()

# cv2.line(imageLine,(200,100),(400,100),(0,255,255),thickness=5,lineType=cv2.LINE_AA)
# plt.imshow(imageLine[:, :, ::-1])
# plt.show()


# imagecopy= image.copy()

# cv2.circle(imagecopy,(600,350),100,(0,0,255),thickness=-2,lineType=cv2.LINE_AA)
# plt.imshow(imagecopy[:,:,::-1])
# plt.show()

# rectangle = image.copy()
# cv2.rectangle(rectangle,(150,300),(250,150,),(255,0,255),thickness=-5,lineType=cv2.LINE_AA)
# plt.imshow(rectangle[:,:,::-1])
# plt.show()

text='Appolo 11 lunching from the USA space station'
font_face = cv2.FONT_HERSHEY_PLAIN
font_scale= -2.3
font_color=(0,255,0)
font_thick=2
img = cv2.putText(image,text,(200,70),font_face,font_scale,font_color,font_thick,cv2.LINE_AA)
plt.imshow(img[:,:,::-1])
plt.show()