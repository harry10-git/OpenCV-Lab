'''SURF is fast when compared to SIFT but not as fast to use with real-time devices like mobile phones
and surveillance cameras. So FAST algorithm was introduced with a very fast computing time. However FAST gives
us only the key points and we may need to compute descriptors with other algorithms like SIFT and SURF.
With a Fast algorithm, we can detect corners and also blobs.'''

import cv2

# Reading the image and converting into B/W
image = cv2.imread('images/sofa.webp')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)

# Drawing the keypoints
kp = fast.detect(gray_image, None)
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0))

cv2.imshow('FAST', kp_image)
cv2.waitKey()