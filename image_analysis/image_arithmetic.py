import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image1 = cv.imread('image1.jpg')
image2 = cv.imread('image2.jpg')
image_rgb1 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)
image_rgb2 = cv.cvtColor(image2, cv.COLOR_BGR2RGB)
resized1 = cv.resize(image_rgb1, (400, 400))
resized2 = cv.resize(image_rgb2, (400, 400))
sum_img = cv.add(resized1, resized2)
plt.subplot(1, 3, 1)
plt.title('Image 1')
plt.imshow(resized1)
plt.subplot(1, 3, 2)
plt.title('Image 2')
plt.imshow(resized2)
plt.subplot(1, 3, 3)
plt.title('Summed Image')
plt.imshow(sum_img)