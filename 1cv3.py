import cv2 as cv

# Function to decrease image size based on a scale factor
def downscale(frame, scale):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dim = (width, height)
    # Use INTER_AREA interpolation for shrinking
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

# Function to increase image size based on a scale factor
def upscale(frame, scale):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dim = (width, height)
    # Use INTER_CUBIC interpolation for enlarging
    return cv.resize(frame, dim, interpolation=cv.INTER_CUBIC)

path = 'Random_image.png'
img = cv.imread(path)

if img is not None:
    # Call the upscale function to double the size
    resized_img = upscale(img, 2) 

    # Print image metadata to the console
    print(f"Original dimensions: {img.shape[:2]}")
    print(f"Resized dimensions: {resized_img.shape[:2]}")
    
    # Show both original and resized versions
    cv.imshow('Original Image', img)
    cv.imshow('Resized Image', resized_img)
    cv.waitKey(0) # Program waits here until you press a key
else:
    print(f"ERROR: Could not find image at {path}")
    print("Check if the file is actually on your Desktop and named correctly.")
