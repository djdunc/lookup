import numpy as np
import cv2
import time
#import imutils
from pylepton import Lepton

# the original image is 80 x 60, 
# this variable is for multiplying that size
resizeFactor = 10

# for capturing data from the module
with Lepton() as l:
    while True: 
      a,_ = l.capture()
      cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast
      np.right_shift(a, 8, a) # fit data into 8 bits
      frame = np.uint8(a)

      # enlarge a bit
      largeFrame = cv2.resize(frame, (80*resizeFactor, 60*resizeFactor))

      # show the frame on window
      cv2.imshow("preview", largeFrame)

      # close window if 'q' key is pressed
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

      # wait this amount of seconds before next frame
      time.sleep(0.1)