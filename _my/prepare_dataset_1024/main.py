import cv2

video_path = "../datasets/nordlandsbanen/"
video_paths = [video_path + "spring.mp4", video_path + "summer.mp4", video_path + "fall.mp4", video_path + "winter.mp4"]
seasons = ["spring", "summer", "fall", "winter"]
output_path = "../datasets/nordlandsbanen_imgs"

VISUALIZE = False

for vp, season in zip(video_paths[0:1], seasons[0:1]):
    cap = cv2.VideoCapture(vp)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total frame count:", total_frames)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Input video width is:", w)
    print("Input video height is:", h)

    img_sz = 1024
    w_from = int((w / 2) - (img_sz / 2))
    w_to = int((w / 2) + (img_sz / 2))
    h_from = int((h / 2) - (img_sz / 2))
    h_to = int((h / 2) + (img_sz / 2))

    start_frame_offset = 4000
    wanted_image_count = 10000
    spacer = int(total_frames / wanted_image_count)
    n_frame = start_frame_offset

    while n_frame < total_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, n_frame)
        ret, frame = cap.read()
        frame_crop = frame[h_from:h_to, w_from:w_to]

        frame_name = f"{n_frame:06d}"
        print("{0} frame: {1}".format(season, frame_name))
        cv2.imwrite("{0}/{1}/{2}.jpg".format(output_path, season, frame_name), frame_crop)

        # if VISUALIZE:
        #     cv2.imshow("frame", frame)
        #     cv2.imshow("frame_crop", frame_crop)
        #
        #     if cv2.waitKey(1) % 256 == 27:
        #         break
        n_frame = n_frame + spacer

    cap.release()
    # if VISUALIZE:
    #     cv2.destroyAllWindows()
