import cv2
import matplotlib.pyplot as plt 

# image = cv2.imread('plansza.jpg',0)

# # plt.imshow(image,cmap='gray')
# # #print(image)
# # print(image[0,0])
# # print(image[0,6])
#zmiana poszczególnych pikseli
# image_copy = image.copy()
# image_copy[2,2] =200
# image_copy[3,2] =200
# image_copy[3,3] =200
# image_copy[4,2] =200

# plt.imshow(image_copy,cmap='gray')
# print(image_copy)
# plt.show()

#Zmiana na kolory z BGR na RGB
img_bgr = cv2.imread('lake.jpg',cv2.IMREAD_COLOR)
img_rgb = img_bgr[:,:,::-1]
# plt.imshow(img_rgb)
# plt.show()
# # cv2.imshow('Obraz przed cięciem: ' , img_bgr)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#wycinanie fragmentu zdfjecia
# cropped_area=img_rgb[40:80,0:40]
#zmiennia rozmiaaru zdjiecia
# width=120
# height=10
# dim=(width,height)

# resized_area = cv2.resize(cropped_area,dsize=dim,interpolation=cv2.INTER_AREA)

#obracanie obrazu 

fliped_1 = cv2.flip(img_rgb,1)
fliped_2 = cv2.flip(img_rgb,0)
fliped_3 = cv2.flip(img_rgb,-1)


plt.figure(figsize=(18, 5))
plt.subplot(141);plt.imshow(fliped_1);plt.title("Horizontal Flip");
plt.subplot(142);plt.imshow(fliped_2);plt.title("Vertical Flip");
plt.subplot(143);plt.imshow(fliped_3);plt.title("Both Flipped");
plt.subplot(144);plt.imshow(img_rgb);plt.title("Original");
plt.show()