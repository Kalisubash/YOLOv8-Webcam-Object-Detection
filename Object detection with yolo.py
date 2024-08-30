import cv2  # Import OpenCV for video processing
from ultralytics import YOLO  # Import the YOLO model from Ultralytics

# Load the YOLOv8 model (you can use 'yolov8n.pt' or another model)
model = YOLO("yolov8n.pt")

# Open the default webcam (0 = default camera, change if using another camera)
cap = cv2.VideoCapture(0)

# Get the video frame dimensions and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Optional: Define the video format and create a VideoWriter object to save the output video
output_path = r"C://Users//ransu//Documents//Python//output_webcam_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # MP4 video codec
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Initialize a set to keep track of unique object IDs
object_track_ids = set()

# Loop to continuously capture frames from the webcam
while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Run YOLOv8 detection on the frame
        results = model.track(frame, persist=True)

        # Iterate over the results for each frame
        for result in results:
            for box in result.boxes:
                # Get the class label of the detected object
                label = model.names[int(box.cls)]
                # Optional: Filter specific objects, for example, 'car' or 'person'
                if label == 'car':  # Change to 'person', 'bike', etc., as needed
                    # Only count if a valid track ID is available
                    if box.id is not None:
                        track_id = int(box.id)
                        # Check if the track ID is new and add it to the set
                        if track_id not in object_track_ids:
                            object_track_ids.add(track_id)
                            # Optionally, increment a counter here

            # Annotate the frame with detected objects
            annotated_frame = result.plot()
            # Display the annotated frame with object labels
            cv2.imshow("YOLOv8 Object Detection", annotated_frame)
            # Write the annotated frame to the output video file
            out.write(annotated_frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release resources after the loop
cap.release()
out.release()
cv2.destroyAllWindows()
