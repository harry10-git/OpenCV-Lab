# binary image thresholding

import cv2 as cv
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv.imread('lenna.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)

# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

cv.imshow('Binary Threshold', thresh1)
cv.imshow('Binary Threshold Inverted', thresh2)
cv.imshow('Truncated Threshold', thresh3)
cv.imshow('Set to 0', thresh4)
cv.imshow('Set to 0 Inverted', thresh5)

cv.waitKey(0)