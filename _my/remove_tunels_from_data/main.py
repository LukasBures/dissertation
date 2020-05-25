import cv2
import os
import shutil
import fnmatch

# seasons = ["spring", "summer", "fall", "winter"]
seasons = ["winter"]
data_path = "../datasets/nordlandsbanen_imgs/"


# tunnel_data_path = "../datasets/nordlandsbanen_imgs/tunnels/"


def th_filter():
    seasons = ["winter"]
    data_path = "../datasets/nordlandsbanen_imgs/"

    for s in seasons:
        data = list()

        for file in os.listdir(data_path + s):
            if fnmatch.fnmatch(file, '*.jpg'):
                img_path = data_path + s + "/" + file
                data.append(img_path)
        data.sort()

        for d in data:
            img = cv2.imread(d)
            img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            sum_img = cv2.sumElems(img_gs)[0] / (img_gs.shape[0] * img_gs.shape[1])

            if sum_img < 50:
                print("--- ", d, sum_img, d.replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))

                # winter
                shutil.move(d, d.replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
                # spring
                shutil.move(d.replace("winter", "spring"), d.replace("winter", "spring").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
                # summer
                shutil.move(d.replace("winter", "summer"), d.replace("winter", "summer").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
                # fall
                shutil.move(d.replace("winter", "fall"), d.replace("winter", "fall").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))

                # cv2.imshow('image', img_gs)
                # if cv2.waitKey(0) % 256 == 32:
                #     continue
            else:
                print(d, sum_img)


def numbers_filter():
    seasons = ["winter"]
    data_path = "../datasets/nordlandsbanen_imgs/"
    img_numbers = ["004000.jpg",
                   "004089.jpg",
                   "004178.jpg",
                   "674971.jpg",
                   "058023.jpg",
                   "058112.jpg",
                   "058201.jpg",
                   "587484.jpg",
                   "057934.jpg",
                   "587217.jpg",
                   "579919.jpg",
                   "785153.jpg",
                   "057845.jpg",
                   "825203.jpg",
                   "554821.jpg",
                   "249373.jpg",
                   "624686.jpg",
                   "645601.jpg",
                   "102256.jpg",
                   "082587.jpg",
                   "044940.jpg",
                   "330452.jpg",
                   "046097.jpg",
                   "045029.jpg",
                   "046275.jpg",
                   "031946.jpg",
                   "031857.jpg",
                   "045919.jpg",
                   "032035.jpg",
                   "045207.jpg",
                   "706477.jpg",
                   "706299.jpg",
                   "046008.jpg",
                   "706388.jpg",
                   "046364.jpg",
                   "046186.jpg",
                   "046542.jpg",
                   "045118.jpg",
                   "706566.jpg",
                   "706922.jpg",
                   "706655.jpg",
                   "706121.jpg",
                   "046631.jpg",
                   "706032.jpg",
                   "322620.jpg",
                   "706210.jpg",
                   "045296.jpg",
                   "046453.jpg",
                   "322531.jpg",
                   "706833.jpg",
                   "706744.jpg",
                   "261566.jpg",
                   "263168.jpg",
                   "712885.jpg",
                   "713597.jpg",
                   "713686.jpg",
                   "707990.jpg",
                   "708079.jpg",
                   "402186.jpg",
                   "045474.jpg",
                   "401029.jpg",
                   "712796.jpg",
                   "332588.jpg",
                   "045741.jpg",
                   "707011.jpg",
                   "705943.jpg",
                   "705854.jpg",
                   "045563.jpg",
                   "402097.jpg",
                   "046720.jpg",
                   "707901.jpg",
                   "707634.jpg",
                   "705676.jpg",
                   "323955.jpg",
                   "705765.jpg",
                   "713063.jpg",
                   "332321.jpg",
                   "707812.jpg",
                   "402275.jpg",
                   "045385.jpg",
                   "058201.jpg",
                   "359911.jpg",
                   "249373.jpg",
                   "463685.jpg",
                   "311940.jpg",
                   "212260.jpg",
                   "742611.jpg",
                   "417227.jpg",
                   "016727.jpg",
                   "301972.jpg",
                   "277497.jpg",
                   "278565.jpg",
                   "564255.jpg",
                   "026695.jpg",
                   "026962.jpg",
                   "026606.jpg",
                   "749464.jpg",
                   "102256.jpg",
                   "289512.jpg",
                   "058112.jpg",
                   "750176.jpg",
                   "057756.jpg",
                   "057667.jpg",
                   "057934.jpg",
                   "056332.jpg",
                   "058112.jpg",
                   "058023.jpg",
                   "056065.jpg",
                   "056510.jpg",
                   "056421.jpg",
                   "055709.jpg",
                   "058201.jpg",
                   "055175.jpg",
                   "055976.jpg",
                   "055442.jpg",
                   "055620.jpg",
                   "057578.jpg",
                   "056866.jpg",
                   "056688.jpg",
                   "056243.jpg",
                   "056154.jpg",
                   "057489.jpg",
                   "055353.jpg",
                   "055798.jpg",
                   "057400.jpg",
                   "055531.jpg",
                   "057133.jpg",
                   "057222.jpg",
                   "055887.jpg",
                   "056955.jpg",
                   "057311.jpg",
                   "055264.jpg",
                   "057044.jpg",
                   "056777.jpg",
                   "559894.jpg",
                   "055086.jpg",
                   "311940.jpg",
                   "212260.jpg",
                   "249373.jpg",
                   "301972.jpg",
                   "275628.jpg",
                   "359911.jpg",
                   "742611.jpg",
                   "796545.jpg",
                   "278565.jpg"]
    
    img_numbers2 = [
        "889194.jpg",
        "889283.jpg",
        "889372.jpg",
        "889461.jpg",
        "889550.jpg",
        "889639.jpg",
        "889728.jpg",
        "889817.jpg",
        "889906.jpg",
        "889995.jpg",
        "890084.jpg",
        "890173.jpg",
        "890262.jpg",
        "890351.jpg",
        "890440.jpg",
        "890529.jpg",
        "890618.jpg",
        "890707.jpg",
        "890796.jpg",
        "890885.jpg",
        "890974.jpg",
        "891063.jpg",
        "891152.jpg",
        "891241.jpg",
        "891330.jpg",
        "891419.jpg",
        "891508.jpg",
        "891597.jpg",
        "891686.jpg",
        "891775.jpg",
        "891864.jpg",
        "891953.jpg",
        "892042.jpg",
        "892131.jpg",
        "892220.jpg",
        "892309.jpg",
        "892398.jpg",
        "892487.jpg",
        "892576.jpg",
        "892665.jpg",
        "892754.jpg",
        "892843.jpg",
        "892932.jpg",
        "893021.jpg",
        "893110.jpg",
        "893199.jpg",
        "893288.jpg",
        "893377.jpg",
        "893466.jpg",
        "893555.jpg",
        "893644.jpg",
        "893733.jpg",
        "893822.jpg",
        "893911.jpg",
        "894000.jpg",
        "894089.jpg"]

    img_numbers = list(dict.fromkeys(img_numbers2))
    for d in img_numbers:
        d = data_path + "winter/" + d

        print("--- ", d, d.replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))

        # winter
        shutil.move(d, d.replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
        # spring
        shutil.move(d.replace("winter", "spring"), d.replace("winter", "spring").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
        # summer
        shutil.move(d.replace("winter", "summer"), d.replace("winter", "summer").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))
        # fall
        shutil.move(d.replace("winter", "fall"), d.replace("winter", "fall").replace("nordlandsbanen_imgs", "nordlandsbanen_imgs/tunnels"))


# th_filter()
numbers_filter()

