import pandas as pd


def load_dataset(path):
    df = pd.read_excel(path)
    X = list(df["text"])
    y = df.drop("text", 1)
    columns = y.columns
    temp = y.apply(lambda item: item > 0)
    y = list(temp.apply(lambda item: list(columns[item.values]), axis=1))
    return X, y
