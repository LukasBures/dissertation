from pprint import pprint

import pretrainedmodels
import timm

print(pretrainedmodels.model_names)
model_names = timm.list_models(pretrained=True)
pprint(model_names)
