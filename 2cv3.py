import cv2 as cv
import numpy as np

# Global variables to track mouse state and drawing preferences
drawing = False
ix, iy = -1, -1
isRectangle = False

# Mouse callback function to handle drawing events
def drawShape(event, x, y, flags, param):
    global ix, iy, drawing, isRectangle

    # On left click, mark starting position and enable drawing mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    # While mouse is moving and button is held down
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            # Draw either a line or rectangle based on the mode
            if not isRectangle:
                cv.line(param, (ix, iy), (x, y), (100, 100, 100), 2)
            else:
                cv.rectangle(param, (ix, iy), (x, y), (100, 100, 100), 2)

    # Disable drawing mode when left button is released
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

# Create blank image and set up mouse interaction
blank = np.zeros((720, 720, 3), dtype=np.uint8)
cv.namedWindow("Moosa")
cv.setMouseCallback("Moosa", drawShape, param = blank)

while True:
    cv.imshow("Moosa", blank)
    key = cv.waitKey(1)

    if key == ord('d'):
        break
    # Toggle between line and rectangle mode on 'c'
    elif key == ord('c'):
        isRectangle = not isRectangle

cv.destroyAllWindows()