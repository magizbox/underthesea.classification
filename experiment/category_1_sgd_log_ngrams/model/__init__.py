import joblib
from os.path import join, dirname
import sys

sys.path.insert(0, dirname(__file__))
from sklearn.preprocessing import normalize

y_transform = joblib.load(join(dirname(__file__), "label.transformer.bin"))
x_transform = joblib.load(join(dirname(__file__), "tfidf.transformer.bin"))
estimator = joblib.load(join(dirname(__file__), "model.bin"))


def identify_dialog_act(X):
    if isinstance(X, list):
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform(X)))
    else:
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform([X])))[0]


def predict_proba(X):
    if isinstance(X, list):
        output = estimator.predict_proba(x_transform.transform(X))
        output_ = normalize(output, axis=1, norm='l1')
        return output_
    else:
        return y_transform.inverse_transform(
            estimator.predict_proba(x_transform.transform([X])))[0]
