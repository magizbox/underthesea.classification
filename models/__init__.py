from os.path import join, dirname

import joblib

y_transform = joblib.load(join(dirname(__file__), "y_transformer.pkl"))
x_transform = joblib.load(join(dirname(__file__), "x_transformer.pkl"))
estimator = joblib.load(join(dirname(__file__), "model.pkl"))


def classifier(X):
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform([X])))[0]
