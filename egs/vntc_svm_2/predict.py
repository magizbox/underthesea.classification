from os.path import dirname, join
import pickle
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

from load_data import load_dataset

cwd = dirname(__file__)
x_transformer_file = open(join(cwd, "snapshots", "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)

y_transformer_file = open(join(cwd, "snapshots", "y_transformer.pkl"), "rb")
y_transformer = pickle.load(y_transformer_file)

ch2_file = open(join(cwd, "snapshots", "ch2.pkl"), "rb")
ch2 = pickle.load(ch2_file)

estimator_file = open(join(cwd, "snapshots", "model.pkl"), "rb")
estimator = pickle.load(estimator_file)


test_path = join(cwd, "data", "test_sample.xlsx")
X_test, y_test = load_dataset(test_path)
y_test = [item for sublist in y_test for item in sublist]
X = x_transformer.transform(X_test)
X = ch2.transform(X)
y = estimator.predict(X)
y_pred = y_transformer.inverse_transform(y)
mlb = MultiLabelBinarizer()
y_pred_1 = mlb.fit_transform([[item] for item in y_pred])
df = pd.concat([
    pd.DataFrame({"text": X_test}),
    pd.DataFrame(y_pred_1, columns=mlb.classes_)
], axis=1)
df.to_excel("data/output.xlsx", index=False)

