""" optical flow motion tracking """
import cv2
cap = cv2.VideoCapture("video.mp4")
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray,100,0.3,7)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p0,None)
    good_new = p1[st==1]
    good_old = p0[st==1]
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        cv2.line(frame,(int(a),int(b)),(int(c),int(d)),(0,255,0),2)
    cv2.imshow('Optical Flow',frame)
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
    if cv2.waitKey(30)==27:
        break
    cap.release()
    cv2.destroyAllWindows()