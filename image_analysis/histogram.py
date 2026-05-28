import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread('image.jpg')
hist_of_image = cv.calcHist([image], [0], None, [255], [0, 256])
hist_equalized_image = cv.equalizeHist(cv.cvtColor(image, cv.COLOR_BGR2GRAY))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.plot(hist_of_image, color = 'gray')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.subplot(1, 2, 3)
plt.title('Equalized Image')
plt.plot(hist_equalized_image, color = 'gray')

plt.show()