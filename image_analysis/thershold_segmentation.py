import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('image.jpg')
_, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
# Display results
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Binary Image')
plt.imshow(binary_image, cmap='gray')
plt.show()