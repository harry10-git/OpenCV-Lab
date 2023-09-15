# gaussian sharpening - subtract blurred img from original

import cv2 as cv

# read img
img = cv.imread('resources/david.jpg')
cv.imshow('normal', img)
cv.waitKey(0)
# blurred img
gaussian = cv.GaussianBlur(img, (7,7), 0)

# apply sharpening method
temp = cv.subtract(img, gaussian)
sharp_img = cv.add(img, temp)

cv.imshow('Sharpened Image', sharp_img)
cv.waitKey(0)
cv.destroyAllWindows()