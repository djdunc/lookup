import cv2
import pylepton
import numpy as np

def record_thermal_video(filename, duration, frame_rate):
    frames = []  # List to store frames for video recording
    recording_frames = duration * frame_rate  # Total frames to capture for the video
    
    with pylepton.Lepton() as camera:
        while True:
            a, b = camera.capture()

            # Normalize the temperature values
            normalized_frame = cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
            
            # Convert the frame to an 8-bit grayscale image
            gray_frame = np.uint8(normalized_frame / 256)
            
            # Record frames for video
            frames.append(gray_frame)
            cv2.imshow('window', gray_frame)
            
            # Check if the recording duration has been reached
            if len(frames) >= recording_frames:
                break

        # Convert frames list to numpy array
        video_frames = np.array(frames)
        
        # Save the video
        #height, width = video_frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify video codec (example: 'mp4v', 'XVID')
        video_writer = cv2.VideoWriter(filename, fourcc, frame_rate, (80, 60))
        
        # Write frames to video file
        for video_frame in video_frames:
            video_writer.write(video_frame)
        
        # Release the video writer
        video_writer.release()

if __name__ == "__main__":
    filename = "thermal_video.mp4"
    duration = 5  # Duration of the video in seconds
    frame_rate = 30  # Frame rate for the video recording
    
    record_thermal_video(filename, duration, frame_rate)
