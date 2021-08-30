import torch
import encoding
import os
import timm
import sys


gpu = 1
model_name = "xception65"
backbone_net = "deeplab_resnest50_ade"

sources = ["/home/lukas/PycharmProjects/Dissertation/datasets/aachen/segmentation_images/day/",
           "/home/lukas/PycharmProjects/Dissertation/datasets/aachen/segmentation_images/night/"]

destinations = [f"/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/segment_{model_name}/day/",
                f"/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/segment_{model_name}/night/"]

for dst in destinations:
    os.makedirs(dst, exist_ok=True)

# sys.stdout = open(f"{destinations[0].replace('day/', '')}segment_{model_name}.log", 'w')

model2 = encoding.models.get_model(backbone_net, pretrained=True).cuda(gpu).eval()
model = timm.create_model(model_name, pretrained=True).cuda(gpu).eval()
print("Model loaded")

for src, dst in zip(sources, destinations):
    for file in os.listdir(src):
        if file.endswith(".jpg"):
            prcs = os.path.join(src, file)
            print("Processing: ", prcs)
            img = encoding.utils.load_image(prcs).unsqueeze(0).cuda(gpu)
            with torch.no_grad():
                output = model(img)
                output2 = model2.evaluate(img)
            print(output.shape)
            print(output2.shape)
            predict = torch.max(output, 1)[1].cpu().numpy() + 1
            mask = encoding.utils.get_mask_pallete(predict, 'citys')
            mask.save(os.path.join(dst, file.replace("jpg", "png")))
print("DONE")

# img = encoding.utils.load_image(filename).cuda().unsqueeze(0)
#

# output = model.evaluate(img)
# predict = torch.max(output, 1)[1].cpu().numpy() + 1
#
# # Get color pallete for visualization
# mask = encoding.utils.get_mask_pallete(predict, 'citys')
# mask.save('output2.png')
