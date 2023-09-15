import cv2 as cv
import numpy as np

img = cv.imread('images/sofa.webp')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Applying SIFT detector
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

# Marking the keypoint on the image using circles
img = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv.imshow('img', img)

cv.waitKey(0)