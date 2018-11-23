import os
from os.path import join, dirname
from random import shuffle


def load_data(folder):
    data = []
    files = [join(folder, x) for x in os.listdir(folder)]
    for file in files:
        topic = file.split("/")[9]
        label = topic.replace(" ", "_")
        name = "__label__" + label
        with open(file, "rb") as f:
            content = f.read()
            content = content.decode('utf-16')
            content = " ".join(i for i in content.split())
            data.append(name + " " + content)
    return data


def convert_to_corpus(name, rows):
    corpus = join(dirname(__file__), "data", "{}.txt".format(name))
    text = "\n".join(row for row in rows)
    with open(corpus, "w") as f:
        f.write(text)


if __name__ == '__main__':
    path = join(dirname(dirname(dirname(__file__))), 'data', "vntc", 'raw')
    train_folder = [join(path, "Train_Full", i) for i in os.listdir(join(path, "Train_Full"))]
    test_folder = [join(path, "Test_Full", i) for i in os.listdir(join(path, "Test_Full"))]
    train = [x for i in train_folder for x in load_data(i)]
    test = [x for i in test_folder for x in load_data(i)]
    convert_to_corpus("train", train)
    convert_to_corpus("test", test)
