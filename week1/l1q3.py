# program to extract rgb values from a pixel

import cv2
import numpy as np

img_grayscale = cv2.imread('rgb.jpg')

b,g,r = cv2.split(img_grayscale)
zeros = np.zeros(b.shape, np.uint8)

img_red = cv2.merge((zeros,zeros,r))
img_green = cv2.merge((zeros,g,zeros))
img_blue = cv2.merge((b,zeros,zeros))


cv2.waitKey(0)
cv2.imshow('blue image',img_blue)
cv2.waitKey(0)
cv2.imshow('red image',img_red)
cv2.waitKey(0)
cv2.imshow('blue image',img_green)
cv2.waitKey(0)

cv2.destroyAllWindows()