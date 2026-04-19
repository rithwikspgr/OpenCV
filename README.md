# OpenCV
A collection of Python scripts exploring computer vision concepts using OpenCV, from basic image processing to real-time object tracking and Haar Cascade face detection.

# OpenCV Python Journey

A collection of computer vision scripts and projects exploring the capabilities of the OpenCV library in Python.

## Contents

### **Lesson 1: Basics & Video Processing**
* `1cv1.py`: Reading and displaying static images.
* `1cv2.py`: Initializing and displaying live webcam feeds.
* `1cv3.py`: Image scaling and interpolation techniques (`INTER_AREA`, `INTER_CUBIC`).
* `1cv4.py`: Converting BGR to RGB for Matplotlib visualization.
* `Extension1.py`: Interactive video feed with pause, reset, and screenshot (Matplotlib) functionalities.

### **Lesson 2: Drawing & Filtering**
* `2cv1.py` & `2cv2.py`: Creating blank canvases and drawing geometric shapes, polygons, and text overlays.
* `2cv3.py`: Interactive drawing application using OpenCV mouse callbacks (`EVENT_LBUTTONDOWN`, `EVENT_MOUSEMOVE`).
* `2cv4.py`: Side-by-side comparison of blurring techniques (Average, Gaussian, Median, Bilateral, Custom 2D Filter).
* `2cv5.py`: Real-time application of a custom 7x7 averaging kernel on a live video feed.

### **Lesson 3: Thresholding & Masks**
* `3cv1.py`: Live video comparison of Regular Thresholding vs. Gaussian Adaptive Thresholding.
* `3cv2.py`: Isolating specific objects using HSV color space boundaries (Color Masking).
* `3cv3.py`: Applying Morphological Opening (Erosion followed by Dilation) to clean up noise in binary masks.

### **Lesson 4: Edge Detection & Contours**
* `4cv1.py`: Extracting structural outlines using the Canny Edge Detector with a custom dynamic thresholding algorithm based on median pixel intensity.
* `4cv2.py`: Object tracking pipeline using `cv.findContours()`, area filtering to remove noise, and `cv.boundingRect()` to draw tracking boxes.

### **Lesson 5: Object & Face Detection**
* `5cv1.py`: Real-time pedestrian tracking using the MOG2 Background Subtractor. Includes morphological closing and contour area filtering for highly accurate bounding boxes.
* `FaceDetection.py`: Implementation of a Haar Cascade Classifier (`haarcascade_frontalface_default.xml`) to detect human faces via live webcam feed using the `detectMultiScale` algorithm.

## 🛠️ Prerequisites
* Python 3.x
* OpenCV (`pip install opencv-python`)
* NumPy (`pip install numpy`)
* Matplotlib (`pip install matplotlib`)

## Notes
* Images and video paths are currently configured for a local macOS environment (`/Users/rithwik/Desktop/...`). To run these scripts, update the file paths to match your local machine.
