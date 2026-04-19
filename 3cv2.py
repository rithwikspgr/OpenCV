import cv2 as cv

img = cv.imread('rubberDuck.png')

# Convert color
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Define the range for 'Yellow' in OpenCV HSV format
lower_yellow = (15, 100, 100)
upper_yellow = (35, 255, 255)

# Create a binary mask where yellow pixels are white and everything else is black
find = cv.inRange(img_hsv, lower_yellow, upper_yellow)

# Show the original image and the resulting mask
cv.imshow('original', img)
cv.imshow('duck found', find)
cv.waitKey(0)
