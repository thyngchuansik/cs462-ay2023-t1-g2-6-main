import cv2
from datetime import datetime
import time

def set_filename():
    # Get the current date and time
    current_datetime = datetime.now()
    # Define the desired format
    formatted_datetime = current_datetime.strftime('%a %b %d %Y %H:%M:%S')
    return formatted_datetime.replace(" ", "_").replace(":","-")

def start_recording():
    # Define the video capture device (0 for the default webcam)
    cap = cv2.VideoCapture(0)

    # Define the codec and create a VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_file = f'{set_filename()}.mp4'
    out = cv2.VideoWriter(f'video/{video_file}', fourcc, 20.0, (640, 480))

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video device")
        exit()

    # Set the duration of the recording in seconds
    duration = 5  # 3 seconds for debugging
    # duration = 10  # 10 seconds

    # Get the current time
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Write the frame to the output video file
        out.write(frame)

        # Display the recorded video in a window (optional)
        cv2.imshow('Recording', frame)

        # Check if the specified duration has elapsed
        if time.time() - start_time >= duration:
            break

        # Press 'q' to stop recording at any time
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()
    return video_file

# start_recording()
