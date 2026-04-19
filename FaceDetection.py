import cv2 as cv

# Create Face Cascade Object
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv.VideoCapture(0)

while True:
    retval, frame = capture.read()
    if not retval:
        break
    # Convert color
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # (base, rescale ratio (1.1 means reduce by 10% each time), 5 minimum neighbours (meaning 5 votes to declare that it's a face))
    face = face_cascade.detectMultiScale(gray_frame, 1.1, 5)

    # Drawing the bounding box around the face
    for (x, y, w, h) in face:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv.imshow('Face Detector', frame)
    if cv.waitKey(1) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()