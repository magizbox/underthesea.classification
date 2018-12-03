import re

import pandas as pd


def tokenize(text):
    parttern = "\w+|[^\w\s]+"
    tokens = re.findall(parttern, text)
    text = " ".join(i for i in tokens)
    return text


def load_dataset(path):
    df = pd.read_excel(path)
    X = list(df["text"])
    X = [tokenize(x) for x in X]
    y = df.drop("text", 1)
    columns = y.columns
    temp = y.apply(lambda item: item > 0)
    y = list(temp.apply(lambda item: list(columns[item.values]), axis=1))
    return X, y
