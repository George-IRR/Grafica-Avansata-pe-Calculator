import cv2
import numpy as np
import os

# PART 1: create a video from 10 frames
latime = 640
inaltime = 480
fps = 5
nume_fisier = 'film_tema.avi'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(nume_fisier, fourcc, fps, (latime, inaltime))

print("Generating 10 frames for video...")
for i in range(10):
    # black background
    frame = np.zeros((inaltime, latime, 3), dtype=np.uint8)

    # moving white square
    x_pos = 50 + (i * 50)
    y_pos = 200
    cv2.rectangle(frame, (x_pos, y_pos), (x_pos+50, y_pos+50), (255, 255, 255), -1)

    out.write(frame)

out.release()
print("Video created successfully!")

# PART 2: read the video and detect the object
print("Playing video and detecting object (press 'q' to quit)...")
cap = cv2.VideoCapture(nume_fisier)

# init FAST detector
fast = cv2.FastFeatureDetector_create()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect keypoints with FAST
    kp = fast.detect(gray, None)

    # draw keypoints in red
    frame_cu_detectie = cv2.drawKeypoints(frame, kp, None, color=(0, 0, 255))

    cv2.imshow('Object Detection in Video', frame_cu_detectie)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()