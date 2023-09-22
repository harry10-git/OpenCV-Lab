'''While Haris and shi-Tomasi are the algorithms to detect the corners of the image.
SIFT is one of the important algorithms that detect objects irrelevant to the scale and rotation
of the image and the reference. This helps a lot while we are comparing the real-world objects to an
image though it is independent of the angle and scale of the image. This method will return
the key points of the images which we need to mark in the image.'''

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