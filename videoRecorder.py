import cv2
import time

cap = cv2.VideoCapture(0)

out = None
out_file = str(int(time.time()))

startRecord = False
started = False

flip = False

while True:
    # Get an image from 'video'
    ret, frame = cap.read()
    if not ret:
        break
    
    # 좌우 반전
    if flip:
        frame = cv2.flip(frame, 1)

    if startRecord:
        cv2.circle(frame, (30,30), radius=10, color=(0,0,255), thickness=-1)
        cv2.putText(frame, 'Record', (50,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,0))
        if not started:
            out = cv2.VideoWriter(out_file+'.avi', cv2.VideoWriter.fourcc(*'XVID'),
                                  20.0, (640,480))
            started = True
        out.write(frame)
    else:
        cv2.putText(frame, 'Preview', (50,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,0))
        if started:
            out.release()
            started = False

    cv2.putText(frame, 'Space: Record, ESC: quit, f: flip', (100, 430),
                cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,0))

    cv2.imshow('Video Record', frame)
    key = cv2.waitKey(1)
    if key == 27: # ESC
        break
    if key == ord(' '):
        startRecord = not startRecord
        out_file = str(int(time.time())) # 현재시간으로 영상을 저장합니다.
    if key == ord('f'):
        flip = not flip

cap.release()
cv2.destroyAllWindows()