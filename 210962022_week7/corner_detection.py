import cv2 as cv
import numpy as np

img = cv.imread('images/sofa.webp')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

result = cv.cornerHarris(gray, 2, 5, 0.07)
result = cv.dilate(result, None)

img[result > 0.01 * result.max()]=[0, 0, 255]
cv.imshow('sofa', img)
cv.waitKey(0)