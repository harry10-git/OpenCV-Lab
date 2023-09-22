'''ORB is a very effective way of detecting the features of the image when compared to SIFT and SURF.
ORB is programmed to find fewer features in the image when compared to the SIFT and SURF algorithm
because it detects the very important features in less time than them yet this algorithm is considered
as a very effective algorithm when compared to other detecting algorithms.'''

import cv2

# Reading the image and converting into B/W
image = cv2.imread('images/sofa.webp')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray_image, None)

# Drawing the keypoints
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0), flags=0)

cv2.imshow('ORB', kp_image)
cv2.waitKey()