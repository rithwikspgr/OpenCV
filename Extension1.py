import cv2 as cv
import matplotlib.pyplot as plt

capture = cv.VideoCapture(0)
paused = False

while True:
    if not paused:
        retval, frame = capture.read()

        if not retval:
            print("End of video reached.")
            paused = True
            continue

        cv.imshow('Interactive Video', frame)
        # (approx 60 FPS)
        key = cv.waitKey(17)
    
    if key == ord('d'):
        break
    # Toggle pause state if 'p' is pressed
    elif key == ord('p'):
        paused = not paused
    # Reset video to the beginning if 'r' is pressed
    elif key == ord('r'):
        capture.set(cv.CAP_PROP_POS_FRAMES, 0)
        paused = False
        print("reset successful")
    # Take a screensshot and show in Matplotlib if 's' is pressed
    elif key == ord('s'):
        img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.title("Captured Frame")
        plt.xlabel("Pixel Width")
        plt.ylabel("Pixel Height")
        plt.show()

capture.release()
cv.destroyAllWindows()