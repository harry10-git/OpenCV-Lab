# python code to apply gaussian blur

import cv2 as cv
img = cv.imread('resources/tiger.jpg')
cv.imshow('Original', img)
cv.waitKey(0)


gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gaussian)
cv.waitKey(0)
cv.destroyAllWindows()