import cv2
import matplotlib.pyplot as plt
from skimage import exposure

# Load images
src = cv2.imread('Photos/lenna.jpg')
ref = cv2.imread('Photos/reference.jpg')

# Convert to grayscale if necessary
if len(src.shape) > 2:
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
else:
    src_gray = src

if len(ref.shape) > 2:
    ref_gray = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
else:
    ref_gray = ref

# Match histograms
matched = exposure.match_histograms(src_gray, ref_gray)

# Plot histograms
plt.hist(src_gray.flatten(), bins=256, range=(0, 256), color='r', alpha=0.5)
plt.hist(ref_gray.flatten(), bins=256, range=(0, 256), color='g', alpha=0.5)
plt.hist(matched.flatten(), bins=256, range=(0, 256), color='b', alpha=0.5)
plt.legend(('Source', 'Reference', 'Matched'), loc='upper right')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# Display images
cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)

cv2.waitKey(0)
cv2.destroyAllWindows()
