import cv2 as cv
import numpy as np

# Function for auto-calculating Canny thresholds
def canny_threshold_values(img, deviation=0.33):
    avgIntense = np.median(img)
    minVal = avgIntense * (1 - deviation)
    maxVal = avgIntense * (1 + deviation)

    return minVal, maxVal

# Function to filter shapes by area and draw rectangles
def filter_contours(min_area, contours):
    for contour in contours:
        # Is countour big enough?
        if cv.contourArea(contour) > min_area:
            # Get x, y coordinates and width, height of the bounding box and draw
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(img_copy,(x, y), (x + w, y + h), (0, 255, 0), 2)

img = cv.imread('blue_ball.jpg')
img_copy = img.copy()
# Blur image to prepare for edge detection
blurred_img = cv.GaussianBlur(img, (3, 3), 0)

# Generate edge map
lowest_val, highest_val = canny_threshold_values(blurred_img)
edges_img = cv.Canny(blurred_img, lowest_val, highest_val)

# Extract a list of shapes (contours) from the edge image
contours, hierarchy = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Run the filter to box the ball
filter_contours(100, contours)
cv.imshow('Boxed Contours', img_copy)
cv.waitKey(0)
cv.destroyAllWindows()

# Note, that the boxing of contour is not working if the image is grayscaled.