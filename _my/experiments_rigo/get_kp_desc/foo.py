spring_cap = cv2.VideoCapture(spring_video_path)
summer_cap = cv2.VideoCapture(summer_video_path)
fall_cap = cv2.VideoCapture(fall_video_path)
winter_cap = cv2.VideoCapture(winter_video_path)

start_frame = 0
spring_cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
summer_cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
fall_cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
winter_cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)


def combine_imgs(img1, img2, img3, img4):
    row1 = np.hstack((img1, img2))
    row2 = np.hstack((img3, img4))
    return np.vstack((row1, row2))


# When everything done, release the capture
spring_cap.release()
summer_cap.release()
fall_cap.release()
winter_cap.release()
cv2.destroyAllWindows()


detector = cv2.AKAZE_create()

while spring_cap.isOpened() & summer_cap.isOpened() & fall_cap.isOpened() & winter_cap.isOpened():
    # Capture frame-by-frame
    spring_ret, spring_frame = spring_cap.read()
    summer_ret, summer_frame = summer_cap.read()
    fall_ret, fall_frame = fall_cap.read()
    winter_ret, winter_frame = winter_cap.read()

    spring_gray = cv2.cvtColor(spring_frame, cv2.COLOR_BGR2GRAY)
    summer_gray = cv2.cvtColor(summer_frame, cv2.COLOR_BGR2GRAY)
    fall_gray = cv2.cvtColor(fall_frame, cv2.COLOR_BGR2GRAY)
    winter_gray = cv2.cvtColor(winter_frame, cv2.COLOR_BGR2GRAY)

    spring_kps, spring_descs = detector.detectAndCompute(spring_gray, None)
    summer_kps, summer_descs = detector.detectAndCompute(summer_gray, None)
    fall_kps, fall_descs = detector.detectAndCompute(fall_gray, None)
    winter_kps, winter_descs = detector.detectAndCompute(winter_gray, None)

    spring_frame_kps = cv2.drawKeypoints(spring_frame, spring_kps, None, color=(0, 255, 0), flags=0)
    summer_frame_kps = cv2.drawKeypoints(summer_frame, summer_kps, None, color=(0, 255, 0), flags=0)
    fall_frame_kps = cv2.drawKeypoints(fall_frame, fall_kps, None, color=(0, 255, 0), flags=0)
    winter_frame_kps = cv2.drawKeypoints(winter_frame, winter_kps, None, color=(0, 255, 0), flags=0)

    spring_resized = cv2.resize(spring_frame_kps, (640, 480))
    summer_resized = cv2.resize(summer_frame_kps, (640, 480))
    fall_resized = cv2.resize(fall_frame_kps, (640, 480))
    winter_resized = cv2.resize(winter_frame_kps, (640, 480))

    # Display the resulting frame
    cv2.imshow("frame", combine_imgs(spring_resized, summer_resized, fall_resized, winter_resized))

    if cv2.waitKey(1) % 256 == 27:
        break
