import joblib
from os.path import join, dirname

y_transform = joblib.load(join(dirname(__file__), "label.transformer.bin"))
x_transform = joblib.load(join(dirname(__file__), "tfidf.transformer.bin"))
estimator = joblib.load(join(dirname(__file__), "model.bin"))

def predict(X):
    if isinstance(X, list):
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform(X)))
    else:
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform([X])))[0]

print(0)