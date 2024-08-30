YOLOv8 Webcam Object Detection
This Python script uses YOLOv8 for real-time object detection via a webcam. It captures live video, performs object detection, and saves the annotated video to a file.

Features
Real-time Object Detection: Uses YOLOv8 to detect and track objects from the webcam feed.
Video Saving: Saves the annotated video to a specified file.
Custom Object Filtering: Allows for detection of specific objects (e.g., cars, persons).
Interactive Display: Shows live video feed with detected objects highlighted.

Requirements
Python 3.x
OpenCV library
YOLOv8 model files
Install the required libraries using pip: pip install opencv-python ultralytics

Usage
Prepare YOLOv8 Model: Download the YOLOv8 model file (yolov8n.pt) and place it in the working directory.
Set Up Output Path: Update the output_path variable in the script to specify where the output video will be saved.
Run the Script:
Capture and Save: The script captures video from the webcam, performs object detection, annotates the video with detected objects, and saves it to the specified file.
Stop Capturing: Press 'q' to stop the script and exit the video capture loop.

Code Overview
Initialization: Loads the YOLOv8 model and initializes webcam capture.
Frame Processing: Captures frames from the webcam, performs object detection, and annotates the frames.
Video Writing: Saves the annotated video to the specified path.
Display and Exit: Displays the live video feed and allows exit by pressing 'q'.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

This README provides a comprehensive overview of the script, including setup, usage, and functionality, tailored for users who want to understand and use your object detection script.

