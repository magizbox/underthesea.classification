import os

from underthesea import word_tokenize
from os.path import join, dirname
from random import shuffle

import pandas as pd


def normalize(text):
    text = text.lower()
    sentence = word_tokenize(text)
    stop_words = open("vietnamese-stopwords.txt").read().split("\n")
    filtered_sentence = [w for w in sentence if not w in stop_words]
    text = " ".join(i for i in filtered_sentence)
    return text


def load_data(folder):
    data = []
    label = folder.split("/")[-1].lower().replace(" ", "_")
    files = [join(folder, x) for x in os.listdir(folder)]
    for file in files:
        with open(file, "rb") as f:
            content = f.read()
            content = content.decode('utf-16')
            content = normalize(content)
        data.append({"label": label, "text": content})
    return data


def convert_to_corpus(name, rows):
    shuffle(rows)
    df = pd.DataFrame(rows)
    onehot = pd.concat([df, pd.get_dummies(df["label"])], axis=1)
    onehot.drop(["label"], axis=1, inplace=True)
    file = join(dirname(dirname(__file__)), "data", "corpus", "{}_.xlsx".format(name))
    onehot.to_excel(file, index=False)

    # output = []
    # labels = list(set([row["label"] for row in rows]))
    # for row in rows:
    #     item = {}
    #     item["text"] = row["text"]
    #     for label in labels:
    #         if label in row["label"]:
    #             item[label] = 1
    #         else:
    #             item[label] = 0
    #     output.append(item)
    # shuffle(output)
    # df = pd.DataFrame(output)
    # columns = ["text"] + labels
    # file = join(dirname(dirname(__file__)), "data", "corpus", "{}.xlsx".format(name))
    # df.to_excel(file, columns=columns, index=False)


if __name__ == '__main__':
    path = join(dirname(dirname(__file__)), 'data', 'raw')
    train_folder = [join(path, "Train_Full", i) for i in os.listdir(join(path, "Train_Full"))]
    test_folder = [join(path, "Test_Full", i) for i in os.listdir(join(path, "Test_Full"))]
    train = [x for i in train_folder for x in load_data(i)]
    test = [x for i in test_folder for x in load_data(i)]
    convert_to_corpus("train", train)
    convert_to_corpus("test", test)
