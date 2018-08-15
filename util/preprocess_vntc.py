from os import listdir, mkdir
from os.path import join, dirname, abspath
import os
import shutil
from underthesea.feature_engineering.text import Text
from underthesea.util.file_io import read, write


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
    root_folder = dirname(dirname(abspath(__file__)))
    print("root folder", root_folder)
    corpus_folder = root_folder + "/tmp/vntc/"
    train_folder = corpus_folder + "train"
    test_folder = corpus_folder + "test"
    train_file = corpus_folder + "train.txt"
    test_file = corpus_folder + "test.txt"
    print("Convert raw data to corpus data")
    try:
        shutil.rmtree(corpus_folder)
    except:
        pass
    finally:
        mkdir(corpus_folder)
        mkdir(corpus_folder + "train")
        mkdir(corpus_folder + "test")
    convert_data(join(root_folder, "data/VNTC/raw/Train_Full"), train_folder)
    convert_data(join(root_folder, "data/VNTC/raw/Test_Full"), test_folder)
    convert_to_fasttext_classification_corpus(train_folder, train_file)
    convert_to_fasttext_classification_corpus(test_folder, test_file)
    shutil.rmtree(train_folder)
    shutil.rmtree(test_folder)


def main():
    create_dataset()


def content_normalize(text):
    return text.replace("\n", " ")


def label_normalize(label):
    return label.lower().replace(" ", "_")


def convert_to_fasttext_classification_corpus(corpus_folder, corpus_file_path):
    try:
        os.remove(corpus_file_path)
    except Exception as e:
        pass
    corpus_file = open(corpus_file_path, "a")
    categories = listdir(corpus_folder)
    for category in categories:
        category_folder = join(corpus_folder, category)
        files = listdir(category_folder)
        for file in files:
            text = open(join(category_folder, file)).read()
            content = content_normalize(text)
            sentence = "__label__{} {}\n".format(label_normalize(category), content)
            corpus_file.write(sentence)


if __name__ == '__main__':
    main()
