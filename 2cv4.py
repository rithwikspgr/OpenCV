import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

garden = cv.imread('garden.png')

avg = cv.blur(garden, (5, 5)) # Simple average blur
gauss = cv.GaussianBlur(garden, (5, 5), 0) # Gaussian blur (weighted)
med = cv.medianBlur(garden, 5) # Median blur (good for salt & pepper noise)
bilateral = cv.bilateralFilter(garden, 9, 75, 75) # Keeps edges sharp

# Define and apply a manual 5x5 averaging kernel
custom_kernel = np.ones((7, 7), np.float32) / 49.0 # used a 7x7 kernel for stronger and more noticeable effect
filter2D = cv.filter2D(garden, -1, custom_kernel)

# Create a grid of subplots to compare results
plt.subplot(231)
plt.imshow(cv.cvtColor(garden, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.xticks([]), plt.yticks([])

plt.subplot(232)
plt.imshow(cv.cvtColor(avg, cv.COLOR_BGR2RGB))
plt.title("Average Blur")
plt.xticks([]), plt.yticks([])

plt.subplot(233)
plt.imshow(cv.cvtColor(gauss, cv.COLOR_BGR2RGB))
plt.title("Gaussian Blur")
plt.xticks([]), plt.yticks([])

plt.subplot(234)
plt.imshow(cv.cvtColor(med, cv.COLOR_BGR2RGB))
plt.title("Median Blur")
plt.xticks([]), plt.yticks([])

plt.subplot(235)
plt.imshow(cv.cvtColor(bilateral, cv.COLOR_BGR2RGB))
plt.title("Bilateral Filter")
plt.xticks([]), plt.yticks([])

plt.subplot(236)
plt.imshow(cv.cvtColor(filter2D, cv.COLOR_BGR2RGB))
plt.title("Filter 2D")
plt.xticks([]), plt.yticks([])

# Final formatting and display
plt.suptitle("Types of Blur Comparison")
plt.tight_layout()
plt.show()

cv.destroyAllWindows()