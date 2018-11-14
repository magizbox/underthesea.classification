import argparse
import os
import sys

from sklearn.model_selection import train_test_split

sys.path.append(os.getcwd())
from time import time
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from sklearn.svm import LinearSVC
from util.load_data import load_dataset


parser = argparse.ArgumentParser("train.py")
parser.add_argument("--train", help="train data path", required=True)
parser.add_argument("-s", "--serialization-dir", help="directory in which to save the model and its logs", required=True)
args = parser.parse_args()

def save_model(filename, clf):
    with open(filename, 'wb') as f:
        joblib.dump(clf, f, compress=2)


train_path = os.path.abspath(args.train)

model_path = os.path.abspath(args.serialization_dir)
print("Load data")
X_train, y_train = load_dataset(train_path)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.8)
target_names = list(set([i[0] for i in y_train]))

print("%d documents (training set)" % len(X_train))
print("%d categories" % len(target_names))

print("Training model")
t0 = time()
transformer = CountVectorizer(ngram_range=(1, 3), max_df=0.7)
X_train = transformer.fit_transform(X_train)

y_transformer = LabelEncoder()
y_train = y_transformer.fit_transform(y_train)


model = LinearSVC()
estimator = model.fit(X_train, y_train)
train_time = time() - t0
print("\t-train time: %0.3fs" % train_time)

save_model(model_path + "/x_transformer.pkl", transformer)
save_model(model_path + "/y_transformer.pkl", y_transformer)
save_model(model_path + "/model.pkl", estimator)
