import cv2
import numpy as np
path="resources/input.png"
image = cv2.imread(path)

image1 = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(minval, maxval, minloc, maxloc) = cv2.minMaxLoc(gray)

cv2.circle(image,maxloc,40,(200,150,0),2)

cv2.imshow("Original Image",image1)
cv2.imshow("Processed Image",image)
cv2.imwrite("bright_spot.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()