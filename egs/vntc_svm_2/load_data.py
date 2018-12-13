import re
import string

import pandas as pd
from pyvi import ViTokenizer


def remove_stopwords(tokens):
    stopwords = open("stopwords.txt").read().split("\n")
    tokens = [i.replace("_", " ") for i in tokens]
    tokens = [i for i in tokens if i not in stopwords]
    text = " ".join(i for i in tokens)
    return text


def remove_punctuation(text):
    text = text.lower()
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    text = re.sub('\s+', ' ', text)
    return text


def normalize(text):
    tokens = ViTokenizer.tokenize(text).split()
    text = remove_stopwords(tokens)
    text = remove_punctuation(text)
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
