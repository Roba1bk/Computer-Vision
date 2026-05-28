import cv2 as cv
import numpy as np
import cv2
img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(binary, kernel, iterations=1)
erosion = cv2.erode(binary, kernel, iterations=1)
cv2.imshow('Dilation', dilation)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
""" Opening and Closing """ 

""" Opening = erosion → dilation (removes small noise)
Closing = dilation → erosion (fills small holes) """
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()