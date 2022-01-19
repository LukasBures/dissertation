import pickle


segmentations_file: str = "/data512/dissertation_results/aachen_all_v1_1/segment_nvidia_v01.pkl"

segmentation_data: dict = dict()
with open(segmentations_file, "rb") as fl:
    while True:
        try:
            data = pickle.load(fl)
            for d in data:
                segmentation_data[d] = data[d]
        except EOFError:
            break
    print("a")


print("ALL DONE")
