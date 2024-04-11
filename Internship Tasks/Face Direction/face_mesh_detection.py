import cv2
import mediapipe as mp
import numpy as np
import time

# Create mediapipe modules and configure parameters
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(
    max_num_faces=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Create instances of mediapipe drawing utilities
mpDrawing = mp.solutions.drawing_utils
drawingSpec = mpDrawing.DrawingSpec((20, 120, 50),
                                    thickness=1,
                                    circle_radius=1)

# Read feed from webcam and resize
cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)

while True:
    isReadOk, frame = cap.read()
    startTime = time.time()

    if not isReadOk:
        print("Couldn't read the feed from webcam.")
        break

    # Get frame dimensions
    frameH, frameW, _ = frame.shape

    # Edit input frame to be RGB and flip it
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frameRGB = cv2.flip(frameRGB, 1)

    # Process the frame
    result = faceMesh.process(frameRGB)

    # Check if results have been acquired
    if result.multi_face_landmarks:
        for faceLandmarks in result.multi_face_landmarks:
            face3D = []
            face2D = []

            for landmark in faceLandmarks.landmark:
                x, y = int(landmark.x * frameW), int(landmark.y * frameH)
                face2D.append([x, y])
                face3D.append([x, y, landmark.z])

            face2D = np.array(face2D, dtype=np.float64)
            face3D = np.array(face3D, dtype=np.float64)

            # Camera matrix
            focalLength = frameW * 1
            cameraMatrix = np.array([[focalLength, 0, frameH / 2],
                                     [0, focalLength, frameW / 2],
                                     [0, 0, 1]])

            # Distortion matrix
            distortionMatrix = np.zeros((4, 1), dtype=np.float64)

            # Solve Perspective-n-Point
            success, rotationVector, translationVector = \
                cv2.solvePnP(face3D, face2D, cameraMatrix, distortionMatrix)

            # Get rotational matrix
            rotationalMatrix, _ = cv2.Rodrigues(rotationVector)

            # Get angles
            angles, _, _, _, _, _ = cv2.RQDecomp3x3(rotationalMatrix)

            # Convert angles to degrees
            x, y, z = angles * 360

            # Display nose direction
            nose2D = (face2D[1][0], face2D[1][1])
            nose3D = (face3D[1][0], face3D[1][1], face3D[1][2])
            nose3DProjection, _ = cv2.projectPoints(np.array([nose3D]),
                                                     rotationVector,
                                                     translationVector,
                                                     cameraMatrix,
                                                     distortionMatrix)
            p1 = (int(nose2D[0]), int(nose2D[1]))
            p2 = (int(nose3DProjection[0][0][0] + y * 30), int(nose3DProjection[0][0][1] - x * 20))
            cv2.line(frame, p1, p2, (255, 255, 255), 8)

            # Draw face mesh
            mpDrawing.draw_landmarks(frame,
                                     faceLandmarks,
                                     mpFaceMesh.FACEMESH_TESSELATION,
                                     drawingSpec,
                                     drawingSpec)

    endTime = time.time()
    fps = 1 / (endTime - startTime)
    cv2.putText(frame, f"FPS: {int(fps)}", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 20, 20), 2)
    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
