import argparse
import logging
import os
from time import time
import numpy as np
from sklearn import metrics

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt

from util.load_data import load_dataset

logging.basicConfig(level=logging.INFO,
                    format='%(asctime) %(levelname)s % (message)s')

# parse commandline argument
parser = argparse.ArgumentParser("benchmark.py")
parser.add_argument("--mode", help="available modes: benchmark", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--transform", help="vectorizer X_train")
parser.add_argument("--s", help="path to save image")
args = parser.parse_args()


def classifier(algorithm, X_train, y_train, X_test, y_test):
    print("_" * 80)
    name = algorithm[0]
    transformer = algorithm[1]
    print(name)
    t0 = time()
    X = transformer.fit_transform(X_train)
    y_transformer = MultiLabelBinarizer()
    y = y_transformer.fit_transform(y_train)

    model = LinearSVC()
    estimator = model.fit(X_train, y_train)
    train_time = time() - t0
    print("\t-train time: %0.3fs" % train_time)

    t0 = time()
    y_pred = estimator.predict(X_test)
    test_time = time() - t0
    print("\t-test time: %0.3fs" % test_time)

    f1_score = metrics.f1_score(y_test, y_pred, average="weighted")
    print("\t-f1 score: %0.3f" % f1_score)

    return name, f1_score, train_time, test_time


if args.mode == "benchmark":
    if not (args.train and args.test):
        parser.error("Mode benchmark requires --train and --test")

    print("Loading from dataset")
    train_path = os.path.abspath(args.train)
    test_path = os.path.abspath(args.test)
    benchmark_path = os.path.abspath(args.s)
    test = args.test
    X_train, y_train = load_dataset(train_path)
    X_test, y_test = load_dataset(test_path)
    target_names = list(set([i[0] for i in y_train]))
    print("%d documents (training set)" % len(X_train))
    print("%d documents (test set)" % len(X_test))
    print("%d categories" % len(target_names))
    print()

    algorithms = []
    t0 = time()
    if args.transform == "tfidf":

        for algo in [
            ("Tfidf Bi-gram", TfidfVectorizer(ngram_range=(1, 2))),
            ("Tfidf Tri-gram", TfidfVectorizer(ngram_range=(1, 3))),
        ]:
            algorithms.append(algo)
        for n in [0.5, 0.6, 0.7, 0.8]:
            algorithms.append(("Tfidf max_df={}".format(str(n)), TfidfVectorizer(max_df=n)))
        for n in [0.5, 0.6, 0.7, 0.8]:
            for ngram in [("Bi-gram", (1, 2)), ("Tri-gram", (1, 3))]:
                algorithms.append(("Tfidf {} + max_df={}".format(ngram[0], str(n)),
                                  TfidfVectorizer(max_df=n, ngram_range=ngram[1])))

    if args.transform == "count":
        for algo in [
            ("Count Bi-gram", CountVectorizer(ngram_range=(1, 2))),
            ("Count Tri-gram", CountVectorizer(ngram_range=(1, 3))),
        ]:
            algorithms.append(algo)
        for n in [0.5, 0.6, 0.7, 0.8]:
            algorithms.append(("Count max_df={}".format(str(n)), CountVectorizer(max_df=n)))
        for n in [0.5, 0.6, 0.7, 0.8]:
            for ngram in [("Bi-gram", (1, 2)), ("Tri-gram", (1, 3))]:
                algorithms.append(("Count {} + max_df={}".format(ngram[0], str(n)),
                                  CountVectorizer(max_df=n, ngram_range=ngram[1])))
    results = []
    print("Benchmark model using linearSVC")
    for algo in algorithms:
        results.append(classifier(algo, X_train, y_train, X_test, y_test))

    # make some plots
    indices = np.arange(len(results))
    results = [[x[i] for x in results] for i in range(4)]
    clf_names, score, training_time, test_time = results
    training_time = np.array(training_time) / np.max(training_time)
    test_time = np.array(test_time) / np.max(test_time)

    plt.figure(figsize=(12, 8))
    plt.title("Score")
    plt.barh(indices, score, .2, label="score", color='navy')
    plt.barh(indices + .3, training_time, .2, label="training time",
             color='c')
    plt.barh(indices + .6, test_time, .2, label="test time", color='darkorange')
    plt.yticks(())
    plt.legend(loc='best')
    plt.subplots_adjust(left=.25)
    plt.subplots_adjust(top=.95)
    plt.subplots_adjust(bottom=.05)

    for i, c in zip(indices, clf_names):
        plt.text(-.3, i, c)
    plt.savefig(benchmark_path)
