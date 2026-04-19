import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
while True:
    retval, frame = capture.read()
    if not retval:
        break

    # Define a custom 5x5 averaging kernel for smoothing
    custom_kernel = np.ones((7, 7), np.float32) / 49.0
    # Blur using custom kernel
    blurred_frame = cv.filter2D(frame, -1, custom_kernel)

    cv.imshow("Blurred Video", blurred_frame)

    if cv.waitKey(1) == ord('d'):
        break

capture.release()
cv.destroyAllWindows