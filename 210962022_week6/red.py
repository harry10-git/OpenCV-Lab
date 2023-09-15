import cv2 as cv
import numpy as np

img = cv.imread('bags.webp')
'''blank = np.zeros((500,500, 3), dtype='uint8') # height , width and number of color channels
cv.imshow('blank', blank)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,50), thickness= cv.FILLED) # img, start, end, bgr, thickness
cv.imshow('Rectangle', blank)'''

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower_color=np.array([100,0,0])
upper_color=np.array([255,90,90])
color_mask=cv.inRange(img,lower_color,upper_color)
seg=cv.bitwise_and(img,img,mask=color_mask)
cv.imshow('',img)
cv.imshow('',seg)




cv.waitKey(0)