import cv2

VISUALIZE = False
SAVE = True

img_names = [
    "2010-10-30_17-47-51_774_input.png",
    "2011-10-01_14-35-34_597_input.png",
    "2011-10-13_14-42-35_909_input.png",
    "2011-10-15_14-27-34_559_input.png",
    "2011-12-29_15-10-33_314_input.png",
    "2012-01-15_14-14-25_544_input.png",
]

path = "/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/segment_nvidia/test/"

for img_name in img_names:
    original = cv2.imread(path + "best_images/" + img_name)
    seg_prediction = cv2.imread(path + "best_images/" + img_name.replace("input", "prediction"))
    mask_s = cv2.imread(path + "sky/" + img_name.replace("_input.png", ".jpg"), 0)
    mask_h = cv2.imread(path + "human/" + img_name.replace("_input.png", ".jpg"), 0)
    mask_v = cv2.imread(path + "vehicle/" + img_name.replace("_input.png", ".jpg"), 0)
    mask_n = cv2.imread(path + "nature/" + img_name.replace("_input.png", ".jpg"), 0)
    mask_shvn = cv2.imread(path + "sky_human_vehicle_nature/" + img_name.replace("_input.png", ".jpg"), 0)
    if VISUALIZE:
        cv2.imshow("mask_shvn original", mask_shvn)

    _, mask_s = cv2.threshold(mask_s, 200, 255, cv2.THRESH_BINARY_INV)
    _, mask_h = cv2.threshold(mask_h, 200, 255, cv2.THRESH_BINARY_INV)
    _, mask_v = cv2.threshold(mask_v, 200, 255, cv2.THRESH_BINARY_INV)
    _, mask_n = cv2.threshold(mask_n, 200, 255, cv2.THRESH_BINARY_INV)
    _, mask_shvn = cv2.threshold(mask_shvn, 200, 255, cv2.THRESH_BINARY_INV)

    result_s = cv2.bitwise_or(original, original, mask=mask_s)
    result_h = cv2.bitwise_or(original, original, mask=mask_h)
    result_v = cv2.bitwise_or(original, original, mask=mask_v)
    result_n = cv2.bitwise_or(original, original, mask=mask_n)
    result_shvn = cv2.bitwise_or(original, original, mask=mask_shvn)

    if VISUALIZE:
        # cv2.imshow("original", original)
        # cv2.imshow("seg_prediction", seg_prediction)
        # cv2.imshow("mask_s", mask_s)
        # cv2.imshow("mask_h", mask_h)
        # cv2.imshow("mask_v", mask_v)
        # cv2.imshow("mask_n", mask_n)
        cv2.imshow("mask_shvn", mask_shvn)
        cv2.imshow("res", result_shvn)
        cv2.waitKey(0)

    if SAVE:
        cv2.imwrite(path + "segmented_sky/" + img_name.replace("_input.png", ".jpg"), result_s)
        cv2.imwrite(path + "segmented_human/" + img_name.replace("_input.png", ".jpg"), result_h)
        cv2.imwrite(path + "segmented_vehicle/" + img_name.replace("_input.png", ".jpg"), result_v)
        cv2.imwrite(path + "segmented_nature/" + img_name.replace("_input.png", ".jpg"), result_n)
        cv2.imwrite(path + "segmented_sky_human_vehicle_nature/" + img_name.replace("_input.png", ".jpg"), result_shvn)
