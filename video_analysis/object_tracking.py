""" object tracking using camshift algorithm """
import cv2
cap = cv2.VideoCapture("video.mp4")
ret, frame = cap.read()
roi = frame[200:300,300:400]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
track_window = (300,200,100,100)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    ret, track_window = cv2.CamShift(dst, track_window,
    (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1))
    pts = cv2.boxPoints(ret)
    pts = pts.astype(int)
    img = cv2.polylines(frame,[pts],True,(0,255,0),2)
    cv2.imshow("Tracking",img)
    if cv2.waitKey(30) & 0xFF == 27:
        break
    cap.release()
    cv2.destroyAllWindows()