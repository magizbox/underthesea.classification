import pandas as pd


def normalize_text(text):
    text = fix_text(text)
    text = " ".join(i for i in text.split())
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    return text.lower()


def load_dataset(path):
    df = pd.read_excel(path)
    X = list(df["text"])
    X = [normalize_text(x) for x in X]
    y = df.drop("text", 1)
    columns = y.columns
    temp = y.apply(lambda item: item > 0)
    y = list(temp.apply(lambda item: list(columns[item.values]), axis=1))
    return X, y
