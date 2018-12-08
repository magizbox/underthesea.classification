import os
from os.path import dirname, join

from language_model import SRILanguageModel

corpus = join(dirname(__file__), "data", "train")
for file in os.listdir(corpus):
    sri_bin = "/usr/share/srilm/bin/i686-m64"
    name = file.replace(" ", "_").replace(".txt", "").lower()
    save_path = f"tmp/model/lm_{name}.bin"
    lm = SRILanguageModel(sri_bin, save_path)
    corpus_path = join(corpus, file)
    lm.fit(corpus_path)
