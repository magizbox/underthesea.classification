import argparse
import os
import sys
from os.path import join, dirname, abspath
from time import time

import fasttext
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))

parser = argparse.ArgumentParser("evaluate.py")
parser.add_argument("--test", help="test data path", required=True)
parser.add_argument("-s", "--serialization-dir", help="directory in which to save the model and its logs",
                    required=True)
args = parser.parse_args()

test_path = os.path.abspath(join(cwd, args.test))
serialization_dir = os.path.abspath(join(cwd, args.serialization_dir))

t0 = time()
classifier = fasttext.load_model('{}/model.bin'.format(serialization_dir))
t1 = time() - t0
print("Load model time: %0.3fs" % t1)
y_true = []
y_predict = []
t1 = time()
for line in open(test_path):
    index = line.find(" ")
    label = line[:index]
    text = line[index + 1:]
    y_true.append(label)
    y_predict.append(classifier.predict([text])[0][0])
print("Accuracy:", round(accuracy_score(y_true, y_predict), 4))
print("Precision:", round(precision_score(y_true, y_predict, average='micro'), 4))
print("Recall   :", round(recall_score(y_true, y_predict, average='micro'), 4))
print("Micro F1 :", round(f1_score(y_true, y_predict, average='micro'), 4))
t2 = time() - t1
print("Predict time: %0.3fs" % t2)

