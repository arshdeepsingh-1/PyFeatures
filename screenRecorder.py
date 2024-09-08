# Import necessary libraries
import cv2
import numpy as np
import pyautogui

# Set the screen size for recording (1920x1080 in this case)
screen_size = (1920, 1080)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, screen_size)

# Variable to control the recording loop
recording = True

print("Screen recording started. Press Ctrl+C to stop.")

try:
    # Main recording loop
    while recording:
        # Take a screenshot
        img = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array
        frame = np.array(img)

        # Convert the frame from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the output video file
        out.write(frame)

except KeyboardInterrupt:
    print("\nScreen recording stopped.")
    recording = False

finally:
    # Release the video writer object and close any OpenCV windows
    out.release()
    cv2.destroyAllWindows()
    print("Video saved as output.mp4")