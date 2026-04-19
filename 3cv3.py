import cv2 as cv
import numpy as np

img = cv.imread('beach.png')
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define sand color range
lower_sand = (10, 20, 100)
upper_sand = (30, 200, 255)
# Generate initial (noisy) mask
find = cv.inRange(hsv_img, lower_sand, upper_sand)

# Create a 5x5 rectangular structuring element (the "brush" for cleaning)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

# Apply 'Opening' (Erosion followed by Dilation) to remove small white noise
# Iterations=13 repeats the process to ensure a cleaner result
Opened = cv.morphologyEx(find, cv.MORPH_OPEN, kernel, iterations=13)

# Comparison raw mask vs. the cleaned version
cv.imshow('Non-opened', find)
cv.imshow('Opened thirteen times', Opened)
cv.waitKey(0)