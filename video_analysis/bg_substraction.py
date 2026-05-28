""" background substraction motion dectection """
import cv2
cap = cv2.VideoCapture("video.mp4")
bg_sub = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    fg_mask = bg_sub.apply(frame)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Foreground mask", fg_mask)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()