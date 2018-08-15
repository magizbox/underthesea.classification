import argparse

from languageflow.evaluation import print_cm
from os.path import join
import os
import fasttext
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score, \
    accuracy_score

from util.convert_to_fasttext_classification_corpus import convert_to_fasttext_classification_corpus

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--mode", help="available modes: train-test, train-test-split, cross-validation", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--train-test-split", type=float,
                    help="train/test split ratio")
parser.add_argument("-s", help="path to save model")
parser.add_argument("--cross-validation", type=int, help="cross validation")
args = parser.parse_args()


if args.mode == "train":
    if not (args.train and args.s):
        parser.error("Mode train-test requires --train and -s")
    train_path = os.path.abspath(args.train)
    model_path = os.path.abspath(args.s)
    fasttext.supervised(train_path, args.s)
    print("Model is saved in {}".format(model_path))

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
    print("Evaluation")
    print("Confusion Matrix")
    for line in open("tmp/test.txt"):
        index = line.find(" ")
        label = line[:index]
        text = line[index + 1:]
        y_true.append(label)
        y_predict.append(classifier.predict([text])[0][0])
    labels = sorted(set(y_true))
    cm = confusion_matrix(y_true, y_predict, labels=labels)
    print_cm(cm, labels=labels)
    print("Classification Report")
    report = classification_report(y_true, y_predict, labels=labels)
    print(report)
    print("Score")
    print("Accuracy:", accuracy_score(y_true, y_predict))
    print("Precision:", precision_score(y_true, y_predict, average='micro'))
    print("Recall   :", recall_score(y_true, y_predict, average='micro'))
    print("Micro F1 :", f1_score(y_true, y_predict, average='micro'))