import os

from os.path import join, dirname
from random import shuffle

import pandas as pd
from ftfy import fix_text


def load_data(folder):
    data = []
    label = folder.split("/")[-1].lower().replace(" ", "_")
    files = [join(folder, x) for x in os.listdir(folder)]
    for i, file in enumerate(files):
        if i % 1000 == 0:
            print(i)
        with open(file, "rb") as f:
            content = f.read()
            content = content.decode('utf-16')
        data.append({"label": label, "text": content})
    return data


def convert_to_corpus(name, rows):
    file = join(dirname(dirname(__file__)), "data", "corpus", "{}.txt".format(name))
    f = open(file, "w")
    for row in rows:
        label = '__label__' + row['label'].replace(" ", " _")
        text = row['text'].replace("\r\n", " ")
        f.write(label + " " + text + "\n")


if __name__ == '__main__':
    path = join(dirname(dirname(__file__)), 'data', "vntc", 'raw')
    train_folder = [join(path, "Train_Full", i) for i in os.listdir(join(path, "Train_Full"))]
    test_folder = [join(path, "Test_Full", i) for i in os.listdir(join(path, "Test_Full"))]
    train = [x for i in train_folder for x in load_data(i)]
    convert_to_corpus("train", train)
    test = [x for i in test_folder for x in load_data(i)]
    convert_to_corpus("test", "Train_Full")
