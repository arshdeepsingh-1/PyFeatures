# Import necessary libraries
import cv2  # OpenCV for computer vision
import time  # Time library (optional, but useful for timing events)

# Open a connection to the default webcam (0 stands for the default camera)
cap = cv2.VideoCapture(0)

# Start an infinite loop to capture frames from the webcam
while True:
    # Capture frame-by-frame from the webcam
    ret, img = cap.read()

    # Flip the image horizontally (1 means flip around the y-axis)
    img = cv2.flip(img, 1, 0)

    # Display the resulting frame in a window called 'webcam'
    cv2.imshow('webcam', img)

    # Wait for 50 milliseconds for a key press (this creates a slight delay for smoother viewing)
    k = cv2.waitKey(50)

    # If the 'ESC' key is pressed (ASCII code 27), break the loop and exit
    if k == 27:
        break

# Release the webcam (free up the resources)
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
