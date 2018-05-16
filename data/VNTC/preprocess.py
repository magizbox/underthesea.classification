import pandas as pd
from os import listdir, mkdir
from os.path import join, dirname
import shutil
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


def convert_data(raw_folder, corpus_folder):
    print(raw_folder)
    for topic in listdir(raw_folder):
        print(topic)
        mkdir(join(corpus_folder, topic))
        for file in listdir(join(raw_folder, topic)):
            content = read_utf16(join(raw_folder, topic, file))
            write(join(corpus_folder, topic, file), content)


def create_dataset():
    print("Convert raw data to corpus data")
    try:
        shutil.rmtree("corpus")
    except:
        pass
    finally:
        mkdir("corpus")
        mkdir("corpus/train")
        mkdir("corpus/test")

    convert_data("raw/Train_Full", "corpus/train")
    convert_data("raw/Test_Full", "corpus/test")


if __name__ == '__main__':
    create_dataset()
