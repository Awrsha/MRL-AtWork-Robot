# Face Mesh Detection and Visualization

This project demonstrates real-time face mesh detection and visualization using the MediaPipe library with OpenCV.

## Features

- Detects and tracks facial landmarks in real-time using the webcam feed.
- Visualizes the detected face mesh with customizable drawing specifications.
- Estimates the direction of the nose by drawing a line from the nose tip to a projected 3D point.
- Displays the frames per second (FPS) of the application.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your_username/face-mesh-detection.git
```

2. Install the required Python dependencies:

```
pip install opencv-python mediapipe numpy
```

## Usage

1. Run the `face_mesh_detection.py` script:

```
python face_mesh_detection.py
```

2. The webcam feed will open up, and you will see the real-time face mesh detection and visualization.

3. Press `q` to exit the application.

## Customization

You can customize various parameters in the script, such as:

- `max_num_faces`: Maximum number of faces to detect.
- `min_detection_confidence`: Minimum confidence score for face detection.
- `min_tracking_confidence`: Minimum confidence score for face tracking.
- Drawing specifications such as color, thickness, and circle radius.

## Acknowledgments

This project utilizes the MediaPipe library for face mesh detection and visualization. Visit the [MediaPipe GitHub repository](https://github.com/google/mediapipe) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
