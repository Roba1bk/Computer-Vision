import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('image.jpg')
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
r, g, b = cv.split(image_rgb)
plt.imshow(r, cmap='Reds')
plt.imshow(g, cmap='Greens')
plt.imshow(b, cmap='Blues')
plt.show()