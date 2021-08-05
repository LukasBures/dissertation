
CODING NOTES
-------------------------------------------------------------------------------------
27.11.2020
- MegaDepth bezi s venvDissertation (jen nejaka hlaska)
- MegaDepth ma vice modelu, 4 + 1 obecnej - prumerujou je, MegaDepth = 2018 CVPR
- Pro barevny obrazky (vymaskovani oblohy - protoze v siti = random) potrebuju: PSPNet
https://github.com/kazuto1011/pspnet-pytorch - je ale stara podle paperswithcode.com je z 2016 a je na 35. pozici (81.2%),
novejsi je HRNet-OCR (85.1%) - pouzije se k vymyskovani pohybujicich trid (lidi, kola, auta, psy, atd) a k vymyskovani oblohy

- https://github.com/kazuto1011/pspnet-pytorch odkazuje na https://github.com/hszhao/PSPNet#usage tam jsou predtrenovane modely:
Download trained models and put them in folder 'evaluation/model':
1 pspnet50_ADE20K.caffemodel: GoogleDrive
2 pspnet101_VOC2012.caffemodel: GoogleDrive
3 pspnet101_cityscapes.caffemodel: GoogleDrive

88.1% mIoU (SS) and 88.6% mIoU (MS) on validation set.
NOTE: 3 points lower than caffe implementation. WIP

SS: averaged prediction with flipping (2x)
MS: averaged prediction with multi-scaling (6x) and flipping (2x)
Both: No CRF post-processing

- konvertovani do torch modelu:
(venvDissertation) lukas@raider:~/PycharmProjects/Dissertation/_segmentation/pspnet-pytorch$ python convert.py -c ./config/voc12_ss.yaml


musi se nastavit pro _segmentation/semantic-segmentation - kod od NVIDIA, asi pocet CPUs
export OMP_NUM_THREADS=12

podle implementace na netu
if 'OMP_NUM_THREADS' not in os.environ:
        current_env["OMP_NUM_THREADS"] = str(int(multiprocessing.cpu_count() / args.nproc_per_node))
- Zprovozneno
(venvDissertation) lukas@raider:~/PycharmProjects/Dissertation/_segmentation/semantic-segmentation$ python -m runx.runx scripts/dump_cityscapes.yml -i

>>> DAY SUMMARY:
- MegaDepth zprovozneno - nutne dodelat vymaskovani oblohy pomoci pspnet-pytorch -> pekne barevne obrazky
- pspnet-pytorch zprovozneno
- semantic-segmentation NVIDIA zprovozneno

-------------------------------------------------------------------------------------
1.12.2020

- naistalovan tensorflow v1.15.4
- nainstaloval lubcudnn7+cu101 + nebude se aktualizovat v balickach
- DeepLabv3+ - https://github.com/tensorflow/models/tree/master/research/deeplab
v _segmentation/tf-models/research/deeplab/deeplab_demo.ipynb je seznam trid ktere jde odfiltrovat

- spocitany obrazky - vizualizace: /home/lukas/PycharmProjects/Dissertation/_segmentation/tf-models/research/deeplab/datasets/pascal_voc_seg/exp/train_on_trainval_set/vis/segmentation_results

>>> DAY SUMMARY:
> funguje DeepLabv3+

-------------------------------------------------------------------------------------
14.12.2020

- https://www.visuallocalization.net/mysubmissions/
My Aachen Day-Night Submissions
Method	day	night	Submission time		
hloc	89.2 / 95.6 / 98.8	84.7 / 92.9 / 100.0	Nov. 19, 2020, 8:36 a.m.	Edit	Delete
superpoint_aachen-superglue_2020.12.11_13.49.06	88.8 / 95.9 / 98.7	85.7 / 92.9 / 100.0	Dec. 14, 2020, 9:17 a.m.
superpoint_max-superglue_2020.12.11_13.50.10	89.4 / 95.8 / 98.8	84.7 / 92.9 / 100.0	Dec. 14, 2020, 9:18 a.m.
superpoint_aachen-my_superglue_2020.12.12_14.58.41	89.6 / 95.6 / 98.8	86.7 / 93.9 / 100.0	Dec. 14, 2020, 9:21 a.m.
superpoint_max-my_superglue_2020.12.12_14.55.50	89.1 / 95.8 / 98.8	85.7 / 92.9 / 100.0	Dec. 14, 2020, 9:22 a.m.

top:
superpoint_aachen-my_superglue_2020.12.12_14.58.41	89.6 / 95.6 / 98.8	86.7 / 93.9 / 100.0	Dec. 14, 2020, 9:21 a.m.

____
SEGMENTATION codes:
Semantic Segmentation on Cityscapes test - nejvic podobnej AACHEN datasetu
https://paperswithcode.com/sota/semantic-segmentation-on-cityscapes

TOP semantic segmentation implementace - https://github.com/NVIDIA/semantic-segmentation
u me je to: /home/lukas/PycharmProjects/Dissertation/_segmentation/semantic_segmentation_NVIDIA

DeepLabv3+
tensorflow - https://github.com/tensorflow/models
https://github.com/tensorflow/models/tree/master/research
https://github.com/tensorflow/models/tree/master/research/deeplab



Prozkoumat:
https://github.com/openseg-group/openseg.pytorch
https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/self_training
https://github.com/naver/kapture + https://arxiv.org/pdf/2007.13867.pdf


>>> DAY SUMMARY:

-------------------------------------------------------------------------------------
16.12.2020

- udelat experimenty s extract_feature: 'd2net-ss':
- samotny zvlast, grayscale, zvetseni, a taky kombinaci

- !!! Dulezite - Nazev metody: semantic segmentation voting / segmentation voting (hlasovani vice segmentacnich metod)
- 


Nvidia semantic-segmentation
https://www.cityscapes-dataset.com/method-details/?submissionID=7836
Cityscapes (85.4 IOU test)


ResNeSt: Cityscapes (83.3 IOU test)
ResNeSt-200 (ours)	Split=Test	(w Mapillary)=yes	mIoU=83.3
(The mIoU is the average between the IoU of the segmented objects over all the images of the test dataset.)
https://github.com/zhanghang1989/ResNeSt
ResNeSt-269	crop=416 pytorch=84.54?? (asi mIoU %)

>>> DAY SUMMARY:
- dalsi dny upravit a pustit v tomhle poradi:
- segment_nvidia.sh (hotovo a je to nejlepsi segmentator)
- segment_resnest.sh (dobre vysledky, je nutne upravit verify_resnest.py a nacist day/night query obrazky)
- segment_deeplab_v3plus.sh (bylo uz zprovozneny)


-------------------------------------------------------------------------------------
17.12.2020
- segment_nvidia.sh - spocitano, v noci to nevypada nic moc
- segment_resnest.sh -  spocitano, v noci to nevypada nic moc
>>> DAY SUMMARY:

-------------------------------------------------------------------------------------
18.12.2020
- https://github.com/lyakaap/NetVLAD-pytorch - netvlad nema trenovani ale je tu tripletloss
- https://github.com/Nanne/pytorch-NetVlad - netvlad ma trenovani ale zatim nevim jak s tim pracovat
>>> DAY SUMMARY:

-------------------------------------------------------------------------------------
20.12.2020
- NetVlad nefunguje mi trenovani, nevim jak
- NetVLAD-pytorch resnet18 nedava dobre vysledky
>>> DAY SUMMARY:
-------------------------------------------------------------------------------------
21.12.2020
- NetVLAD-pytorch vgg16 nedava dobre vysledky

-- clanek 2019: From Coarse to Fine: Robust Hierarchical Localization at Large Scale
- https://arxiv.org/pdf/1812.03506.pdf
- Aachen: pro den SFM je nejlepsi SIFT model, pro noc je nejlepsi jejich:  NetVlad+SuperPoint


>>> DAY SUMMARY:
-------------------------------------------------------------------------------------









Experiment idea:
- detekovat n (4096/nebo vic) KP a pak filtrovat - vic se jich odfiltruje pryc
- netvlad, spustit clustering na day/night/day+night
- filtraci pomoci semanticke segmentace pouzit jen na day, na night je na nic







Running DeepLab on Cityscapes Semantic Segmentation Dataset
https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/cityscapes.md


