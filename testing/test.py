import cv2
import numpy as np
import pylepton
import time

recording_duration = 2  # Duration of each video recording segment in seconds
frame_rate = 30  # Frame rate for the video recording
recording_frames = recording_duration * frame_rate  # Total frames to capture for each recording
frame_counter = 0  # Counter to keep track of frames captured  

# Create a Lepton camera object
with pylepton.Lepton() as lepton:
	video_writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(80,60), False)
		
	
	# Loop over frames from the camera
	
	
	while True:
		a,b = lepton.capture() # a is the data buffer, b is the frame id based on sum of buffer vals
				
		frame = cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
		scaled_frame = cv2.resize(frame, None, fx=1, fy=1)
		cv2.imshow('window', scaled_frame)
		np.right_shift(frame, 8, frame)
				
		# Create video writer object
		
		
		#fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Specify video codec (example: 'mp4v', 'XVID')
		#video_writer = cv2.VideoWriter('videos/test.avi', fourcc, 30, (80, 60))
				
		video_writer.write(frame)
		
		frame_counter += 1

		if frame_counter >= (recording_frames):
			# Release the video writer
			video_writer.release()
			print("writer released")
			break
		
		# Wait for a key press
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# Clean up resources
cv2.destroyAllWindows()


