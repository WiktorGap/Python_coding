import cv2
import os 
import matplotlib.pyplot as plt
import numpy as np

# img_brg= cv2.imread('New_Zealand_Coast.jpg',cv2.IMREAD_COLOR)
# img_rgb = cv2.cvtColor(img_brg,cv2.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
# plt.show()

# #brightness

# # matrix = np.ones(img_rgb.shape,dtype='uint8') * 50
# # img_rgb_brighter = cv2.add(img_rgb,matrix)
# # img_rgb_darker = cv2.subtract(img_rgb,matrix)

# # plt.figure(figsize=[18, 5])
# # plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Darker")
# # plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original")
# # plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Brighter")

# plt.show()

#contrast

# matrix1 = np.ones(img_rgb.shape) * 0.8
# matrix2=np.ones(img_rgb.shape) * 1.2

# img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb),matrix1))
# img_rgb_brighter = np.uint8(cv2.multiply(np.float64(img_rgb),matrix2))


# plt.figure(figsize=[18,5])
# plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Lower Contrast")
# plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original")
# plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Higher Contrast")

# plt.show()

# matrix1=np.ones(img_rgb.shape)*0.8
# matrix2=np.ones(img_rgb.shape)*1.2

# img_lower=np.uint8(cv2.multiply(np.float64(img_rgb),matrix1))
# img_rgb_higher = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2), 0, 255))

# plt.figure(figsize=[18,5])
# plt.subplot(131); plt.imshow(img_lower); plt.title('lower contrast')
# plt.subplot(132); plt.imshow(img_rgb);plt.title('orginal')
# plt.subplot(133); plt.imshow(img_rgb_higher);plt.title('high contrast')
# plt.show()

# img_read = cv2.imread('building-windows.jpg',cv2.IMREAD_GRAYSCALE)
# tetcal , img_tresh = cv2.threshold(img_read,100,255,cv2.THRESH_BINARY)

# # Show the images
# plt.figure(figsize=[18, 5])

# plt.subplot(121);plt.imshow(img_read, cmap="gray");  plt.title("Original")
# plt.subplot(122);plt.imshow(img_tresh, cmap="gray");plt.title("Thresholded")

# print(img_tresh.shape)
# plt.show()


# img=cv2.imread('piano.png',cv2.IMREAD_GRAYSCALE)
# retval  , img_thresh_gb_1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
# retval  , img_thresh_gb_2=cv2.threshold(img,130,255,cv2.THRESH_BINARY)
# img_thresh_adp = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# # Show the images
# plt.figure(figsize=[18,15])
# plt.subplot(221); plt.imshow(img,        cmap="gray");  plt.title("Original");
# plt.subplot(222); plt.imshow(img_thresh_gb_1,cmap="gray");  plt.title("Thresholded (global: 50)");
# plt.subplot(223); plt.imshow(img_thresh_gb_2,cmap="gray");  plt.title("Thresholded (global: 130)");
# plt.subplot(224); plt.imshow(img_thresh_adp,  cmap="gray");  plt.title("Thresholded (adaptive)");
# plt.show()

img_rec = cv2.imread('rectangle.jpg',cv2.IMREAD_GRAYSCALE)
img_cir = cv2.imread('circle.jpg',cv2.IMREAD_GRAYSCALE)

# plt.figure(figsize=[20, 5])
# plt.subplot(121);plt.imshow(img_rec, cmap="gray")
# plt.subplot(122);plt.imshow(img_cir, cmap="gray")
# print(img_rec.shape)
# plt.show()

# result = cv2.bitwise_and(img_rec,img_cir,mask=None)
# plt.imshow(result, cmap="gray")
# plt.show()

# result = cv2.bitwise_or(img_rec,img_cir,mask=None)
# plt.imshow(result, cmap="gray")
# plt.show()


# result = cv2.bitwise_xor(img_rec,img_cir,mask=None)
# plt.imshow(result, cmap="gray")
# plt.show()

img_brg=cv2.imread('coca-cola-logo.png')
img_rgb=cv2.cvtColor(img_brg,cv2.COLOR_BGR2RGB)
#print(img_rgb.shape)
logo_w = img_rgb.shape[0]
logo_h = img_rgb.shape[1]
img_back_brg =cv2.imread('checkerboard_color.png')
img_back_rgb=cv2.cvtColor(img_back_brg,cv2.COLOR_BGR2RGB)

aspect_ratio = logo_w / img_back_rgb.shape[1]
dim = (logo_w,int(img_back_rgb.shape[0]*aspect_ratio))

img_back_rgb = cv2.resize(img_back_brg,dim,interpolation=cv2.INTER_AREA)
#plt.imshow(img_back_rgb)
#plt.show()

img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)
retval , img_mask = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# plt.imshow(img_mask, cmap="gray")
# plt.show()

img_mask_inv = cv2.bitwise_not(img_mask)
# plt.imshow(img_mask_inv, cmap="gray")
# plt.show()
img_background = cv2.bitwise_and(img_back_rgb,img_back_rgb,mask=img_mask)
# plt.imshow(img_background)
# plt.show()

img_foreground = cv2.bitwise_and(img_rgb, img_rgb, mask=img_mask_inv)
plt.imshow(img_foreground)
plt.show()

result = cv2.add(img_background, img_foreground)
plt.imshow(result)
plt.show()
cv2.imwrite("logo_final.png", result[:, :, ::-1])