import argparse
import os
from time import time

import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.svm import LinearSVC

from util.load_data import load_dataset
from util.model_evaluation import get_metrics

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--mode", help="available modes: train-test, train-test-split, cross-validation", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--chi2", help="select some number of features using a chi-squared test", type=int)
parser.add_argument("--s", help="path to save model")
parser.add_argument("--train_size", type=float,
                    help="train/test split ratio")
args = parser.parse_args()


def save_model(filename, clf):
    with open(filename, 'wb') as f:
        joblib.dump(clf, f, compress=3)


if args.mode == "train-test":
    if not (args.train and args.test):
        parser.error("Mode train-test requires --train and --test")
    if not args.s:
        parser.error("Mode train-test requires --s ")
    if not args.train_size:
        parser.error("Mode train-test requires --train_size")
    train_path = os.path.abspath(args.train)
    test_path = os.path.abspath(args.test)

    print("Train model")
    train_size = args.train_size
    model_path = os.path.abspath(args.s)
    print("Load data")
    X_train, y_train = load_dataset(train_path)
    X_test, y_test = load_dataset(test_path)

    target_names = list(set([i[0] for i in y_train]))

    print("%d documents (training set)" % len(X_train))
    print("%d documents (test set)" % len(X_test))
    print("%d categories" % len(target_names))
    print()

    print("Training model")
    t0 = time()
    transformer = CountVectorizer(ngram_range=(1, 3), max_df=0.7)
    X_train = transformer.fit_transform(X_train)

    y_transformer = MultiLabelBinarizer()
    y_train = y_transformer.fit_transform(y_train)

    X_test = transformer.transform(X_test)
    y_test = y_transformer.transform(y_test)

    model = OneVsRestClassifier(LinearSVC())

    estimator = model.fit(X_train, y_train)
    train_time = time() - t0
    print("\t-train time: %0.3fs" % train_time)

    t0 = time()
    y_pred = estimator.predict(X_test)
    test_time = time() - t0
    print("\t-test time: %0.3fs" % test_time)

    get_metrics(y_test, y_pred)
    save_model(model_path + "/x_transformer.pkl", transformer)
    save_model(model_path + "/y_transformer.pkl", y_transformer)
    save_model(model_path + "/model.pkl", estimator)
