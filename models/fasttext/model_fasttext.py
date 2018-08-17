from os.path import join, dirname

import fasttext as ft

filepath = join(dirname(__file__), "vntc_20180602.model.bin")
model = ft.load_model(filepath)


def tranform_output(y):
    y = y[0].replace("__label__", "")
    y = y.replace("-", " ")
    return y


def classify(X):
    labels = model.predict([X])
    label = [tranform_output(item) for item in labels]
    return label
