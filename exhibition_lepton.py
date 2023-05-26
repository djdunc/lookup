#!/usr/bin/python

import cv2
import numpy as np
import pylepton
import time


# Define a function to convert the raw infrared data to a colorized video feed
def mono(frame):
    # Convert the raw frame data to a grayscale image
    gray = cv2.normalize(frame, frame, 0, 65535, cv2.NORM_MINMAX)
    return gray

# Create a window for the video and make it full screen
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


# Create a Lepton camera object
with pylepton.Lepton() as lepton:
    # Loop over frames from the camera
    while True:
        # Capture a raw infrared frame from the camera
        a,b = lepton.capture() # a is the data buffer, b is the frame id based on sum of buffer vals
        
        # Calculate temperature statistics
        min_temp = (np.min(a)* 0.01) - 273.15
        max_temp = (np.max(a)* 0.01) - 273.15
        # Display temperature values
        #print("Min:", round(min_temp,1), "Max:", round(max_temp,1))

        # Convert the raw frame data to a colorized video feed
        frame = mono(a)
        # Scale up the colorized video feed by a factor of 10
        scaled_frame = cv2.resize(frame, None, fx=10, fy=10)
        #print(scaled_frame.shape[1])
        # Overlay the text on the frame
        cv2.putText(scaled_frame, str(round(min_temp)), (5, scaled_frame.shape[0] - 20), cv2.FONT_HERSHEY_DUPLEX, 0.6, 0xffff, 2)
        cv2.putText(scaled_frame, str(round(max_temp)), (5, 30), cv2.FONT_HERSHEY_DUPLEX, 0.6, 0xffff, 2)
        cv2.imshow('window', scaled_frame)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean up resources
cv2.destroyAllWindows()

