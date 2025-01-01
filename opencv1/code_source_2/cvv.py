# Import Libraries
import os
import cv2
import math
import glob
import numpy as np
import matplotlib.pyplot as plt

# Find keypoints in all images
# Find pairwise correspondences
# Estimate pairwise Homographies
# Refine Homographies
# Stitch with Blending

imagefiles = glob.glob(f"boat{os.sep}*")
imagefiles.sort()
images=[]
for filename in imagefiles:
    img=cv2.imread(filename,cv2.COLOR_BGR2RGB)
    images.append(img)

num_images=len(imagefiles)
plt.figure(figsize=[30,10])
num_cols = 3
num_rows=math.ceil(num_images/num_cols)
for i in range(0,num_images):
    plt.subplot(num_rows,num_cols,i+1)
    plt.axis("off")
    plt.imshow(images[i])


sticher = cv2.Stitcher_create()
status,result = sticher.stitch(images)
if status ==0:
    plt.figure(figsize=[30, 10])
    plt.imshow(result)
plt.show()