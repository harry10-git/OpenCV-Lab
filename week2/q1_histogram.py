# read an image and provide histogram equalization
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('hist.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([img], [0], None, [256], [0, 256])

cv.imshow('original image', img)
plt.plot(hist)
plt.show()


eq_img = cv.equalizeHist(img)
hist2 = cv.calcHist([eq_img], [0], None, [256], [0, 256])
plt.plot(hist2)
plt.show()
cv.imshow('Histogram equilization', eq_img)
cv.waitKey(0)
cv.destroyAllWindows()

