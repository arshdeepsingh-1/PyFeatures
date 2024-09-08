# Import necessary libraries
import cv2  # OpenCV for video processing
import numpy as np  # NumPy for array manipulations
import pyautogui  # PyAutoGUI for taking screenshots

# Set the screen size for recording (1920x1080 in this case)
screen_size = (1920, 1080)

# Define the codec (XVID codec for .mp4 file) and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # XVID is a popular codec for .mp4
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, screen_size)  # 20.0 is the frame rate (FPS)

# Infinite loop to continuously capture the screen
while True:
    # Take a screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array for OpenCV processing
    frame = np.array(img)

    # Convert the frame from BGR (used by OpenCV) to RGB (used by screenshots)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output video file
    out.write(frame)

    # Check if the 'q' key is pressed to stop the recording
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video writer object and close any OpenCV windows
out.release()
cv2.destroyAllWindows()
