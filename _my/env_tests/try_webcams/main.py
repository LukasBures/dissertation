import numpy as np
import cv2

cap0 = cv2.VideoCapture(0, cv2.CAP_V4L)  # Trust Webcam
cap1 = cv2.VideoCapture(1, cv2.CAP_V4L)  # Microsoft Webcam
cap2 = cv2.VideoCapture(2, cv2.CAP_V4L)  # Creative Depth Sensor

while True:
    # Capture frame-by-frame
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    frame0 = cv2.resize(frame0, (640, 480))
    frame1 = cv2.resize(frame1, (640, 480))
    frame2 = cv2.resize(frame2, (640, 480))

    horizontal0 = cv2.flip(frame0, 1)
    horizontal1 = cv2.flip(frame1, 1)
    horizontal2 = cv2.flip(frame2, 1)

    img = np.hstack((np.hstack((horizontal0, horizontal1)), horizontal2))

    # Display the resulting frame
    cv2.imshow("frame", img)

    if cv2.waitKey(1) % 256 == 27:
        break

# When everything done, release the capture
cap0.release()
cap1.release()
cap2.release()
cv2.destroyAllWindows()
