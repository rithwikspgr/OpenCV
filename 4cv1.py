import cv2 as cv
import numpy as np

# Statistical function to calculate Canny thresholds based on median intensity
def canny_threshold_values(img, deviation=0.33):
    # Find the median pixel intensity
    avgIntense = np.median(img) #
    # Calculate low and high thresholds using a 33% buffer
    minVal = avgIntense * (1 - deviation)
    maxVal = avgIntense * (1 + deviation)

    return minVal, maxVal

# Load and prepare image
img = cv.imread('dog.png')
# Canny requires a grayscale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Apply blur to reduce background noise (Note: 1x1 kernel is used here)
blurred_img = cv.GaussianBlur(gray_img, (1, 1), 0)

# Get auto-calculated thresholds
lowest_val, highest_val = canny_threshold_values(blurred_img)
# Detect edges
edges_img = cv.Canny(blurred_img, lowest_val, highest_val)

cv.imshow('Edges', edges_img)
cv.waitKey(0)
cv.destroyAllWindows