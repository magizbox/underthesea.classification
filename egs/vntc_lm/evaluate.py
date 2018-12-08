import os
from os.path import join, dirname

srilm_path = "/usr/share/srilm/bin/i686-m64"

model_path = join(dirname(__file__), "tmp")
model_name = [i for i in os.listdir(model_path) if i.endswith(".bin")]