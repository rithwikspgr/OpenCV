import cv2 as cv

# Initialize video capture from the default webcam (index 0)
capture = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    retval, frame = capture.read()
    
    # If the frame was not grabbed successfully, exit the loop
    if not retval:
        break
        
    # Display the resulting live video frame
    cv.imshow('Live Video', frame)
    
    # Check if the 'd' key is pressed to exit the loop
    if cv.waitKey(1) == ord('d'):
        break

# Release the capture device and close all active windows
capture.release() 
cv.destroyAllWindows()