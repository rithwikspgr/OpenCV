import cv2 as cv
import matplotlib.pyplot as plt

path = 'Random_image.png'
img = cv.imread(path)

if img is not None:
    # Convert image from BGR (OpenCV default) to RGB (Matplotlib default)
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Use Matplotlib to display the image
    plt.imshow(rgb_img)

    # Configure plot labels and titles
    plt.title('Task 4: Matplotlib Display')
    plt.xlabel('Pixel Width')
    plt.ylabel('Pixel Height')

    # Render the plot
    plt.show()
    cv.waitKey(0)