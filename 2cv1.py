import cv2 as cv
import numpy as np

# Create a 500x500 black canvas with 3 color channels
blank = np.zeros((500, 500, 3), dtype = 'uint8')

# (image, start, end, color, thickness)
cv.line(blank, (1,1), (100, 100), (164, 78, 89), 5)

# Draw a hollow rectangle (image, top-left, bottom-right, color, thickness)
cv.rectangle(blank, (450, 450), (300, 300), (78, 92, 56), 3)

# Draw a solid circle (image, center, radius, color, thickness=-1 for fill)
cv.circle(blank, (250, 250), 50, (34, 89, 74), -1)

# Create an array of points for a custom polygon/line
pts = np.array([(8, 430), (7, 85)], np.int32)
# Draw the polygon line
cv.polylines(blank, [pts], False, (100, 92, 18), 13)

# Display the final canvas
cv.imshow('Random Shapes', blank)
cv.waitKey(0)