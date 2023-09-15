import cv2 as cv
import imutils

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

image = cv.imread('images/bolt.webp')

image = imutils.resize(image,width=min(400, image.shape[1]))

# Detecting all the regions in the
# Image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(image,winStride=(2, 2),padding=(4, 4),scale=1.05)

for (x, y, w, h) in regions:
    cv.rectangle(image, (x, y),
                  (x + w, y + h),
                  (0, 0, 255), 2)

cv.imshow("Image", image)
cv.waitKey(0)