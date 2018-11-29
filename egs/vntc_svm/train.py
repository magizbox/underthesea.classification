import argparse
import os
import pickle
import sys
from os.path import dirname, join, abspath
cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))
from time import time
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from util.load_data import load_dataset

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--train", help="train data path", required=True)
parser.add_argument("-s", "--serialization-dir", help="directory in which to save the model and its logs",
                    required=True)
args = parser.parse_args()


def save_model(filename, clf):
    pickle.dump(clf, open(filename, 'wb'))


train_path = os.path.abspath(join(cwd, args.train))
serialization_dir = os.path.abspath(join(cwd, args.serialization_dir))
print("Load data")
X_train, y_train = load_dataset(train_path)
# X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.8)
target_names = list(set([i[0] for i in y_train]))

print("%d documents" % len(X_train))
print("%d categories" % len(target_names))

print("Training model")
t0 = time()
transformer = TfidfVectorizer(ngram_range=(1, 2), max_df=0.7)
X_train = transformer.fit_transform(X_train)

y_transformer = LabelEncoder()
y_train = [item for sublist in y_train for item in sublist]
y_train = y_transformer.fit_transform(y_train)

model = LinearSVC()
estimator = model.fit(X_train, y_train)
t1 = time() - t0
print("Train time: %0.3fs" % t1)

t0 = time()
save_model(serialization_dir + "/x_transformer.pkl", transformer)
save_model(serialization_dir + "/y_transformer.pkl", y_transformer)
save_model(serialization_dir + "/model.pkl", estimator)
t1 = time() - t0
print("Save model time: %0.3fs" % t1)