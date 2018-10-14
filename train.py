import argparse
import os
import pickle
from time import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.svm import LinearSVC

from util.load_data import load_dataset
from util.model_evaluation import get_metrics

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--mode", help="available modes: train-test, train-test-split, cross-validation", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--s", help="path to save model")
parser.add_argument("--train_size", type=float,
                    help="train/test split ratio")
args = parser.parse_args()


def save_model(filename, clf):
    with open(filename, 'wb') as f:
        pickle.dump(clf, f, pickle.HIGHEST_PROTOCOL)


if args.mode == "train-test":
    if not (args.train and args.test):
        parser.error("Mode train-test requires --train and --test")
    train_path = os.path.abspath(args.train)
    test_path = os.path.abspath(args.test)
    train_size = args.train_size
    model_path = os.path.abspath(args.s)
    if not os.path.exists(model_path):
        os.mkdir(model_path)
    test = args.test
    print("Load data")
    X_train, y_train = load_dataset(train_path)
    X_test, y_test = load_dataset(test_path)
    X = X_train + X_test
    y = y_train + y_test
    target_names = list(set([i[0] for i in y]))
    print("%d documents (training set)" % len(X_train))
    print("%d documents (test set)" % len(X_test))
    print("%d categories" % len(target_names))
    print()

    print("Training model")
    t0 = time()
    transformer = CountVectorizer(ngram_range=(1, 2))
    X = transformer.fit_transform(X)
    y_transformer = MultiLabelBinarizer()
    y = y_transformer.fit_transform(y)

    model = OneVsRestClassifier(LinearSVC())
    X_train, X_dev, y_train, y_dev = train_test_split(X, y, train_size=train_size)
    estimator = model.fit(X_train, y_train)
    train_time = time() - t0
    print("\t-train time: %0.3fs" % train_time)

    t0 = time()
    y_pred = estimator.predict(X_dev)
    test_time = time() - t0
    print("\t-test time: %0.3fs" % test_time)

    get_metrics(y_dev, y_pred)
    save_model(model_path + "count.transformer.pkl", transformer)
    save_model(model_path + "y_transformer.pkl", y_transformer)
    save_model(model_path + "model.pkl", estimator)
