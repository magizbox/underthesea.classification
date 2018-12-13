import sys
from os.path import dirname, abspath, join
from time import time
cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))
import pickle
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from util.load_data import load_dataset
from util.model_evaluation import get_metrics, plot_confusion_matrix

t0 = time()
x_transformer_file = open(join(cwd, "snapshots", "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)
y_transformer_file = open(join(cwd, "snapshots", "y_transformer.pkl"), "rb")
y_transformer = pickle.load(y_transformer_file)
ch2_file = open(join(cwd, "snapshots", "ch2.pkl"), "rb")
ch2 = pickle.load(ch2_file)
estimator_file = open(join(cwd, "snapshots", "model.pkl"), "rb")
estimator = pickle.load(estimator_file)
duration = time() - t0
print("Load model time: %0.3fs" % duration)

test_path = join(cwd, "data", "test.xlsx")
X_test, y_test = load_dataset(test_path)
t0 = time()
y_test = [item for sublist in y_test for item in sublist]
X = x_transformer.transform(X_test)
X = ch2.transform(X)
y = estimator.predict(X)
y_pred = y_transformer.inverse_transform(y)
duration = time() - t0
print("Predict time: %0.3fs" % duration)
get_metrics(y_test, y_pred)

classes = set(y_test)
cm = confusion_matrix(y_test, y_pred)
plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues)
