import cv2 as cv

# Read the image from the specified file path
img = cv.imread('Random_image.png');

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not find the image file. Check the filename and folder!")
else:
    # Display the image in a window named 'perfff'
    cv.imshow('perfff', img)
    # Wait indefinitely for a key press before closing the window
    cv.waitKey(0)