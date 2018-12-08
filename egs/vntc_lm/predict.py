from os import listdir
from os.path import join

from language_model import SRILanguageModel


class LMClassifier:
    def __init__(self, srilm_path, serialization_dir):
        self.lms = {}
        for file in listdir(serialization_dir):
            name = file.split(".")[0][3:]
            model_path = join(serialization_dir, file)
            lm = SRILanguageModel(sri_bin=srilm_path, savepath=model_path)
            self.lms[name] = lm

    def predict(self, filepath):
        best_label = None
        max_score = None
        for label, lm in self.lms.items():
            score = lm.predict(filepath)
            print(f"{label} -> {score}")
            if max_score is None:
                max_score = score
                best_label = label
            if score > max_score:
                max_score = score
                best_label = label
        return best_label


srilm_path = "/usr/share/srilm/bin/i686-m64"
serialization_dir = "tmp/model"
classifier = LMClassifier(srilm_path, serialization_dir)


folder = "data/test/Khoa hoc"
files = listdir(folder)
files = [join(folder, file) for file in files]
for file in files:
    y_pred = classifier.predict(file)
    print(y_pred)
