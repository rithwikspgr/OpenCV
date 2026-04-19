import cv2 as cv
import numpy as np

capture = cv.VideoCapture('People_Moving_Airport.mp4')

# Create object that wil act as background subtracter
background_sub = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

while True:
    retval, frame = capture.read()
    if not retval:
        break 
    
    # Use the created object on each frame read
    bg_mask = background_sub.apply(frame)
    ret, cleaned = cv.threshold(bg_mask, 254, 255, cv.THRESH_BINARY)

    # Create custom kernel and use it for morphology closing
    custom_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    cleaned = cv.morphologyEx(cleaned, cv.MORPH_CLOSE, custom_kernel, iterations=2)

    # (base, mode, method)
    contours, hierarchy = cv.findContours(cleaned, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #check if contour satisfies size constraints and extract coordinates and dimensions to create a bounding box
    for contour in contours:
        if cv.contourArea(contour) > 200:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow('Movement (Cleaned)', cleaned)
    cv.imshow('Pedestrians', frame)

    if cv.waitKey(30) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

""" Note - it is possible to obtain different results from different combintations of kernel sizes (I'm using (5, 5) which is working the best),
morphology closing iterations (I'm using 2) and minimum contour area (I'm using 200)."""
