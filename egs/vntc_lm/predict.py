import argparse
import os
from os.path import join, dirname

from language_model import SRILanguageModel

parser = argparse.ArgumentParser("predict.py")
file = parser.add_argument_group("The following arguments are mandatory for file option")
file.add_argument("--fin", help="text file input")
args = parser.parse_args()


output = []
srilm_path = "/usr/share/srilm/bin/i686-m64"

model_path = join(dirname(__file__), "tmp")
model_name = [i for i in os.listdir(model_path) if i.endswith(".bin")]
for path in model_name:
    model = join(model_path, path)
    lm = SRILanguageModel(sri_bin=srilm_path, savepath=model)
    file_path = args.fin
    result = lm.predict(file_path)
    output.append(result)
max_score = max(output)
predict = model_name[output.index(max(output))]
label = predict.replace("lm_", "").replace(".bin", "").replace("_", " ")
print(label)
