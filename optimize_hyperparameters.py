import argparse
import logging
import os
from time import time
import warnings

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

from util.load_data import load_dataset

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime) %(levelname)s % (message)s')

# parse commandline argument
parser = argparse.ArgumentParser("benchmark.py")
parser.add_argument("--mode", help="available modes: benchmark", required=True)
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--trans", help="vectorizer X_train")
args = parser.parse_args()


if not (args.train and args.test):
    parser.error("Mode benchmark requires --train and --test")
if not args.trans:
    parser.error("Mode benchmark require --trans")


def grid_search(pipeline, train_path, test_path):
    X_train, y_train = load_dataset(train_path)
    X_test, y_test = load_dataset(test_path)
    target_names = list(set([i[0] for i in y_train]))
    print("%d documents (training set)" % len(X_train))
    print("%d documents (test set)" % len(X_test))
    print("%d categories" % len(target_names))
    print()

    gridsearch = GridSearchCV(pipeline, parameters, cv=1,
                              n_jobs=-1, verbose=1)

    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    print(parameters)
    t0 = time()
    gridsearch.fit(X_train, y_train)
    print("done in %0.3fs" % (time() - t0))
    print()
    print("Best dev score: %0.3f" % gridsearch.best_score_)
    print("Best parameters set:")
    best_parameters = gridsearch.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
    print("Best test score: %0.3f" % gridsearch.score(X_test, y_test))


if __name__ == '__main__':
    print("Loading from dataset")
    train_path = os.path.abspath(args.train)
    test_path = os.path.abspath(args.test)

    pipeline_tfidf = Pipeline([
        ("vect", TfidfVectorizer()),
        ("clf", LinearSVC()),
    ])
    pipeline_count = Pipeline([
        ("vect", CountVectorizer()),
        ("clf", LinearSVC()),
    ])
    parameters = {
        'vect__max_df': (0.5, 0.6, 0.7, 0.8),
        'vect__ngram_range': ((1, 2), (1, 3)),
    }

    if args.trans == "tfidf":
        grid_search(pipeline_tfidf, train_path, test_path)

    if args.trans == "count":
        grid_search(pipeline_count, train_path, test_path)
