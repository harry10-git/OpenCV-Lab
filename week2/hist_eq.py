# perform histogram equilisation
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Photos/dark.jpg',1)
cv.imshow('original', img)
cv.waitKey(0)
cv.destroyAllWindows()

#Histogram Equalization
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",grayimg)
cv.waitKey(0)
cv.destroyAllWindows()
equ = cv.equalizeHist(grayimg)
cv.imshow("Histogram Equalized",equ)
cv.waitKey(0)
cv.destroyAllWindows()


plt.hist(grayimg.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.hist(equ.flatten(),256,[0,256], color = 'g')
plt.xlim([0,256])
plt.legend(('Original','Equalized Histogram'), loc = 'upper left')
plt.show()


