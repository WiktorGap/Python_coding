import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def readImagesandTimes():
    filenames=["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]

    times = np.array([1 / 30.0, 0.25, 2.5, 15.0],dtype=np.float32)

    images = []
    for filename in filenames:
        im = cv2.imread(filename)
        images.append(im)
    return images , times

images,times = readImagesandTimes()

alignMTB = cv2.createAlignMTB()
alignMTB.process(images,images)

calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images,times)

x = np.arange(256,dtype=np.uint8)
y = np.squeeze(responseDebevec)

ax = plt.figure(figsize=(30, 10))
plt.title("Debevec Inverse Camera Response Function", fontsize=24)
plt.xlabel("Measured Pixel Value", fontsize=22)
plt.ylabel("Calibrated Intensity", fontsize=22)
plt.xlim([0, 260])
plt.grid()
plt.plot(x, y[:, 0], "r", x, y[:, 1], "g", x, y[:, 2], "b")

mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images,times,responseDebevec)

tonemapDrago = cv2.createTonemapDrago(1.0,0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3 * ldrDrago
plt.figure(figsize=(20, 10));plt.imshow(np.clip(ldrDrago, 0, 1));plt.axis("off")
plt.show()
#cv2.imwrite("ldr-Drago.jpg", 255*ldrDrago[:, :, ::-1])
print("saved ldr-Drago.jpg")