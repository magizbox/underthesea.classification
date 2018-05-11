import os
from os import listdir
# noinspection PyUnresolvedReferences
from os.path import join


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
        print(category)
        category_folder = join(corpus_folder, category)
        files = listdir(category_folder)
        for file in files:
            text = open(join(category_folder, file)).read()
            content = content_normalize(text)
            sentence = "__label__{} {}\n".format(label_normalize(category), content)
            corpus_file.write(sentence)


if __name__ == '__main__':
    corpus_folder = "../data/TC201805/corpus"
    corpus_file_path = "train.txt"
    convert_to_fasttext_classification_corpus(corpus_folder, corpus_file_path)
