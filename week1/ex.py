#import the cv2 lib
import cv2

# to read a image
img_grayscale = cv2.imread("messi.jpg",0)

# cv2.imshow to show image in a window
cv2.imshow('grayscale image', img_grayscale)

# waitkey waits for a press to close window and 0 in indefinite loop
cv2.waitKey(0)

#destroy all windows created
cv2.destroyAllWindows()

# to write an image
cv2.imwrite('messi2.jpg', img_grayscale)

