# log transformation
import cv2 as cv
import numpy as np

img = cv.imread('log.jpg')

# applying log transformation
c = 255 / (np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# specify the data type
log_transformed = np.array(log_transformed, dtype=np.uint8)

# save the output
cv.imwrite('log_transformed.jpg', log_transformed)
