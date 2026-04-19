import cv2 as cv
import numpy as np

# Canvas and shape initialization
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.line(blank, (1,1), (100, 100), (164, 78, 89), 5)
cv.rectangle(blank, (450, 450), (300, 300), (78, 92, 56), 3)
cv.circle(blank, (250, 250), 50, (34, 89, 74), -1)

pts = np.array([(8, 430), (7, 85)], np.int32)
cv.polylines(blank, [pts], False, (100, 92, 18), 13)

# Overlay text on the image (image, text, position, font, scale, color, thickness)
cv.putText(blank, "This is ezz", (0, 50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (90, 1, 90), 3)

cv.imshow('Random Shapes', blank)
cv.waitKey(0)