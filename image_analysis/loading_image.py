import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('image.jpg')
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.subplot(2, 2, 1)
plt.title('bgr Image')
plt.imshow(image)
plt.subplot(2, 2, 2)
plt.title('rgb Image')
plt.imshow(image_rgb)
plt.subplot(2, 2, 3)
plt.title('gray Image')
plt.show()