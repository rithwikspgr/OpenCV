import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    retval, frame = capture.read()
    # Convert color
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Regular Thresholding: applies a fixed threshold value (150) to the entire image
    ret, regular_thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    
    # Adaptive Thresholding: calculates thresholds for smaller regions to handle varying light
    # Uses a 11x11 neighborhood (block size) and Gaussian weighting
    adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)

    # Display the two different thresholding results
    cv.imshow('Regular Threshold', regular_thresh)
    cv.imshow('Adaptive Threshold', adaptive_thresh)

    if cv.waitKey(20) == ord('d'):
        break

capture.release
cv.destroyAllWindows