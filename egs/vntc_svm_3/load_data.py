import re

import pandas as pd


def tokenize(text):
    parttern = "\w+|[^\w\s]+"
    tokens = re.findall(parttern, text)
    return tokens


def remove_stopwords(text):
    stopwords = open("stopwords.txt").read().split("\n")
    pattern = re.compile(r'\b(' + r'|'.join(stopwords) + r')\b\s*')
    text = pattern.sub(' ', text)
    return text


def normalize(text):
    text = remove_stopwords(text)
    tokens = tokenize(text)
    text = " ".join(i for i in tokens)
    return text


def load_dataset(path):
    df = pd.read_excel(path)
    X = list(df["text"])
    X = [normalize(x) for x in X]
    y = df.drop("text", 1)
    columns = y.columns
    temp = y.apply(lambda item: item > 0)
    y = list(temp.apply(lambda item: list(columns[item.values]), axis=1))
    return X, y
