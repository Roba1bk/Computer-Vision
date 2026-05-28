import cv2
import os
video_path = "video.mp4"
output_folder = "frames"
if not os.path.exists(output_folder):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video")
        exit()
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    if frame is not None:
        cv2.imwrite(filename, frame)
        frame_count +=1
        print('total frame extracted: ', frame_count)
        cap.release()