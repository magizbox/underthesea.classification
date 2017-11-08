import pandas as pd
from underthesea.feature_engineering.text import Text


def load_dataset(data_file):
    df = pd.read_excel(data_file)
    X = list(df["text"])

    def convert_text(x):
        try:
            return Text(x)
        except:
            pass
        return ""

    X = [convert_text(x) for x in X]
    y = df.drop("text", 1)
    # labels = Y.columns
    columns = y.columns
    temp = y.apply(lambda _: _ > 0)
    y = list(temp.apply(lambda _: list(columns[_.values]), axis=1))
    return X, y
