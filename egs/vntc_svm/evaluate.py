from os.path import dirname, join
import pickle
from sklearn.metrics import f1_score

from util.load_data import load_dataset

cwd = dirname(__file__)
x_transformer_file = open(join(cwd, "snapshots", "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)

y_transformer_file = open(join(cwd, "snapshots", "y_transformer.pkl"), "rb")
y_transformer = pickle.load(y_transformer_file)

estimator_file = open(join(cwd, "snapshots", "model.pkl"), "rb")
estimator = pickle.load(estimator_file)

test_path = join(cwd, "data", "test.xlsx")
X_test, y_test = load_dataset(test_path)
y_test = [item for sublist in y_test for item in sublist]
X = x_transformer.transform(X_test)
y = estimator.predict(X)
y_pred = y_transformer.inverse_transform(y)

print("f1_score:", f1_score(y_test, y_pred, average='weighted'))