import cv2
import numpy as np
import pylepton

# Define a function to convert the raw infrared data to a colorized video feed
def colorize(frame):
    # Convert the raw frame data to a grayscale image
    gray = cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
    # Apply a colormap to the grayscale image to create a colorized version
    color = cv2.applyColorMap(np.uint8(gray / 256), cv2.COLORMAP_JET)
    return color

# Create a Lepton camera object
with pylepton.Lepton() as lepton:
    # Loop over frames from the camera
    while True:
        # Capture a raw infrared frame from the camera
        #frame = lepton.capture()
        a,b = lepton.capture() # a is the data buffer, b is the frame id based on sum of buffer vals
        # Convert the raw frame data to a colorized video feed
        color_frame = colorize(a)
        # Scale up the colorized video feed by a factor of 10
        scaled_frame = cv2.resize(color_frame, None, fx=20, fy=20)
        # Display the colorized video feed in a window
        cv2.imshow('Lepton', scaled_frame)
        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up resources
cv2.destroyAllWindows()
