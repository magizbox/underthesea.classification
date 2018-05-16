import argparse
from os.path import join
import os
import fasttext
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score

from util.convert_to_fasttext_classification_corpus import convert_to_fasttext_classification_corpus

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--mode", help="available modes: train-test, train-test-split, cross-validation", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--train-test-split", type=float,
                    help="train/test split ratio")
parser.add_argument("--cross-validation", type=int, help="cross validation")
args = parser.parse_args()

if args.mode == "train-test":
    if not (args.train and args.test):
        parser.error("Mode train-test requires --train and --test")
    train_path = os.path.abspath(args.train)
    print("Convert train data")
    convert_to_fasttext_classification_corpus(train_path, "tmp/train.txt")
    test_path = os.path.abspath(args.test)
    print("Convert test data")
    convert_to_fasttext_classification_corpus(train_path, "tmp/test.txt")
    test = args.test
    print("Train model")
    classifier = fasttext.supervised('tmp/train.txt', 'tmp/model.bin')
    classifier = fasttext.load_model("tmp/model.bin.bin")
    y_true = []
    y_predict = []
    for line in open("tmp/test.txt"):
        index = line.find(" ")
        label = line[:index]
        text = line[index+1:]
        y_true.append(label)
        y_predict.append(classifier.predict([text])[0][0])
    report = classification_report(y_true, y_predict)
    print(report)
    print("Precision:", precision_score(y_true, y_predict, average='micro'))
    print("Recall   :", recall_score(y_true, y_predict, average='micro'))
    print("Micro F1 :", f1_score(y_true, y_predict, average='micro'))
quit(0)


if args.cross_validation:
    print(args.cross_validation + 1)