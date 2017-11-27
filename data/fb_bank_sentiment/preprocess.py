from os.path import join, dirname
import json
import pandas as pd
import numpy as np
from underthesea.util.file_io import read


def filter_post(post):
    if len(post["sentiment"]) > 0:
        return True
    else:
        return False


def transform_post(post):
    post["meta"] = json.loads(post["meta"])
    try:
        post["sentiment"] = json.loads(post["sentiment"])
    except:
        post["sentiment"] = []
    post["sentiment"] = list(
        set([item["polarity"] for item in post["sentiment"] if item["polarity"]]))
    return post


def get_row(post):
    row = {}
    row["text"] = post["text"]
    row["labels"] = post["sentiment"]
    return row


def convert_to_corpus(rows):
    data = []
    labels = list(set(sum([row["labels"] for row in rows], [])))
    for row in rows:
        item = {}
        item["text"] = row["text"]
        for label in labels:
            if label in row["labels"]:
                item[label] = 1
            else:
                item[label] = 0
        data.append(item)
    df = pd.DataFrame(data)
    n = df.shape[0]
    train_size = 0.8
    split = int(train_size * n)
    data_file = join(dirname(__file__), "corpus", "data.xlsx")
    train_file = join(dirname(__file__), "corpus", "train.xlsx")
    test_file = join(dirname(__file__), "corpus", "test.xlsx")
    columns = ["text"] + labels
    df.to_excel(data_file, index=False, columns=columns)
    df.ix[:split, :].to_excel(train_file, index=False, columns=columns)
    df.ix[split:, :].to_excel(test_file, index=False, columns=columns)


def raw_to_corpus():
    file = join(dirname(__file__), "raw", "sentiments.json")
    data = read(file)
    posts = json.loads(data)
    posts = [transform_post(p) for p in posts]
    posts = [p for p in posts if filter_post(p)]
    np.random.shuffle(posts)
    rows = [get_row(p) for p in posts]
    convert_to_corpus(rows)


if __name__ == '__main__':
    raw_to_corpus()
