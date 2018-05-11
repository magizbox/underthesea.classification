import pandas as pd
from os import listdir

from os.path import join, dirname

from sklearn.utils import shuffle
from underthesea.feature_engineering.text import Text
from underthesea.util.file_io import read, write
import json
from functools import reduce


def read_utf16(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        content = content.decode("utf-16")
        return Text(content)


def transform_text(text, label, labels):
    output = {}
    output["text"] = text
    output["label"] = 1
    for l in labels:
        output[l] = 1 if l == label else 0
    return output


def create():
    # train dataset
    FOLDER = dirname(__file__)
    data_folder = join(FOLDER, "data", "Train_Full")
    labels = listdir(data_folder)
    dataset = []
    for label in labels:
        folder = join(data_folder, label)
        files = listdir(folder)
        texts = [read_utf16(join(folder, file)) for file in files]
        items = [transform_text(text, label, labels) for text in texts]
        dataset += items
    columns = ["text"] + labels
    df = pd.DataFrame(dataset, columns=columns)
    df.to_excel("data/data.xlsx", index=False, encoding="utf-8")


def sample_dataset():
    df = pd.read_excel("data/data.xlsx")
    df.sample(10000).to_excel("data/data_10k.xlsx", index=False,
                              encoding="utf-8")


def create_fasttext_datafile(filename, X, y):
    lines = ["__label__{} , {}".format(y_, x_) for x_, y_ in zip(X, y)]
    content = "\n".join(lines)
    write(filename, content)


def create_fasttext_dataset(datafile, output):
    df = pd.read_excel(datafile)
    df = shuffle(df)
    X = list(df["text"])

    def convert_text(x):
        try:
            return Text(x)
        except:
            pass
        return ""

    X = [convert_text(x) for x in X]
    X = [x.replace("\n", " ") for x in X]
    Y = df.drop("text", 1)
    columns = Y.columns
    Y = Y.apply(lambda x: x > 0)
    Y = list(Y.apply(lambda x: "".join(list(columns[x.values])), axis=1))
    Y = [_.replace(" ", "-") for _ in Y]
    test_size = 0.2
    split = int(len(X) * (1 - test_size))
    X_train = X[:split]
    X_test = X[split:]
    Y_train = Y[:split]
    Y_test = Y[split:]
    create_fasttext_datafile("{}_train.txt".format(output), X_train, Y_train)
    create_fasttext_datafile("{}_test.txt".format(output), X_test, Y_test)
    pass


if __name__ == '__main__':
    # create_dataset()
    # sample_dataset()

    # datafile = "data/data_3k.xlsx"
    # output = "ft_3k"
    datafile = "data/data_10k.xlsx"
    output = "ft_10k"
    # datafile = "data/data.xlsx"
    # output = "ft_30k"

    create_fasttext_dataset(datafile, output=output)
