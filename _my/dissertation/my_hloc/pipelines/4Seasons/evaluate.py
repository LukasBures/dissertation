from pathlib import Path

from utils2 import evaluate_submission

relocalization_files = {
    "training": "RelocalizationFilesTrain/relocalizationFile_recording_2020-03-24_17-36-22.txt",
    "validation": "RelocalizationFilesVal/relocalizationFile_recording_2020-03-03_12-03-23.txt",
    "test0": "RelocalizationFilesTest/relocalizationFile_recording_2020-03-24_17-45-31_*.txt",
    "test1": "RelocalizationFilesTest/relocalizationFile_recording_2020-04-23_19-37-00_*.txt",
}
ref_dir = Path("/data512/datasets/4Seasons/reference")
root_dir = Path("/data512/dissertation_results/4Seasons-2022.02.02_09.14.49/results_train")
submission_dir = root_dir / "submission_superpoint+superglue"
reloc = ref_dir / relocalization_files["training"]

print("Evaluating the relocalization submission ...")
evaluate_submission(submission_dir=Path(submission_dir), relocs=Path(reloc), ths=[0.1, 0.2, 0.5])

# evaluate_submission_filtering(submission_dir=submission_dir, relocs=reloc, ths=[0.1, 0.2, 0.5])
