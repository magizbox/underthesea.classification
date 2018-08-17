from sklearn.externals import joblib
import pickle


def save_model(filename, clf):
    with open(filename, 'wb') as f:
        pickle.dump(clf, f, pickle.HIGHEST_PROTOCOL)


def load_model(filename):
    pass


def save_transformer():
    pass


def load_transformer():
    pass
