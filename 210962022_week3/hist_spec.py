import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def histogram_specification(input_img, ref_img):
    hist_input = cv.calcHist([input_img], [0], None, [256], [0, 256])
    hist_ref = cv.calcHist([ref_img], [0], None, [256], [0, 256])
    hist_input /= hist_input.sum()
    hist_ref /= hist_ref.sum()
    cdf_input = hist_input.cumsum()
    cdf_ref = hist_ref.cumsum()
    lut = np.interp(cdf_input, cdf_ref, np.arange(256))
    output_img = cv.LUT(input_img, lut).astype(np.uint8)
    return output_img, hist_input, hist_ref

input_path = "resources/input.png"
reference_path = "resources/reference.png"
input_image=cv.imread(input_path)
reference_image=cv.imread(reference_path)
output_image, hist_input, hist_ref = histogram_specification(input_image, reference_image)

plt.figure(figsize=(15,8))

plt.subplot(2, 3, 1)
plt.imshow(cv.imread(input_path, cv.IMREAD_GRAYSCALE))
plt.title('Input Image')

plt.subplot(2, 3, 2)
plt.imshow(cv.imread(reference_path, cv.IMREAD_GRAYSCALE))
plt.title('Reference Image')

plt.subplot(2, 3, 3)
plt.imshow(output_image, cmap='gray')
plt.title('Histogram Specified Image')

plt.subplot(2, 3, 4)
plt.plot(hist_input)
plt.title('Histogram of Input Image')

plt.subplot(2, 3, 5)
plt.plot(hist_ref)
plt.title('Histogram of Reference Image')

plt.subplot(2, 3, 6)
hist_output = cv.calcHist([output_image], [0], None, [256], [0, 256])
plt.plot(hist_output)
plt.title('Histogram of Specified Image')

plt.tight_layout()
plt.show()