# sobel and laplacian sharpening - use pattern images

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('resources/french_window.jpg')
cv.imshow('original', img)
cv.waitKey(0)

# sobel
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

temp = np.sqrt(sobelX**2, sobelY**2)
temp = temp.astype(np.uint8)

sharpened_img = cv.add(img, temp)
cv.imshow('sobel', sharpened_img)
cv.waitKey(0)

# laplacian
laplacian_temp = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian_temp = laplacian_temp.astype(np.uint8)
laplacian_img = cv.add(img, laplacian_temp)
cv.imshow('laplacian', laplacian_img)
cv.waitKey(0)

cv.destroyAllWindows()