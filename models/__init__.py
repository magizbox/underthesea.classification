import pickle
from os.path import join, dirname


y_transform = pickle.load(open(join(dirname(__file__), "y_transformer.pkl"), "rb"))
x_transform = pickle.load(open(join(dirname(__file__), "x_transformer.pkl"), "rb"))
estimator = pickle.load(open(join(dirname(__file__), "model.pkl"), "rb"))


def classifier(X):
        return y_transform.inverse_transform(
            estimator.predict(x_transform.transform([X])))[0]
