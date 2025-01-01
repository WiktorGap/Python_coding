import cv2
import matplotlib.pyplot as plt 
# image = cv2.imread('cocacola.png',1)
# print(image)
# print("---------")
# print(image.dtype)
# print("---------")
# print(image.shape)


# imagep_plt = plt.imshow(image,cmap='gray')
# plt.show()
# print(imagep_plt)

# img_NZ_bgr = cv2.imread("lake.jpg", cv2.IMREAD_COLOR)


# b, g, r = cv2.split(img_NZ_bgr)

# Show the channels
# plt.figure(figsize=[20, 5])

# plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
# plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
# plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# Merge the individual channels into a BGR image
# imgMerged = cv2.merge((b, g, r))
# Show the merged output
# plt.subplot(144)
# plt.imshow(imgMerged[:, :, ::-1])
# plt.title("Merged Output")
# plt.show()