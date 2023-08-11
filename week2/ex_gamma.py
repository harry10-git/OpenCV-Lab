# gamma transformation
import cv2 as cv
import numpy as np

# open
img = cv.imread('gamma.jpg')

# trying 4 gamma values
for gamma in [0.1,0.5,1.2,2.2]:
    # apply gamma correction
    gamma_corrected = np.array(255*(img/255) ** gamma, dtype='uint8')

    cv.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)