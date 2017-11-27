from os.path import join, dirname
import json
import pandas as pd

from underthesea.util.file_io import read


def filter_post(post):
    if len(post["act"]) > 0:
        return True
    else:
        return False


def transform_post(post):
    post["meta"] = json.loads(post["meta"])
    post["act"] = json.loads(post["act"])
    post["act"] = list(set([act["name"] for act in post["act"] if act["name"]]))
    return post


def get_row(post):
    row = {}
    row["text"] = post["text"]
    row["labels"] = post["act"]
    return row


def remove_illegal_value(df):
    pass


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
    df = remove_illegal_value()
    n = df.shape[0]
    train_size = 0.8
    split = int(train_size * n)
    train_file = join(dirname(__file__), "corpus", "train.xlsx")
    test_file = join(dirname(__file__), "corpus", "test.xlsx")
    columns = ["text"] + labels
    df.ix[:split, :].to_excel(train_file, index=False, columns=columns)
    df.ix[split:, :].to_excel(test_file, index=False, columns=columns)


def raw_to_corpus():
    file = join(dirname(__file__), "raw", "acts.json")
    data = read(file)
    posts = json.loads(data)
    posts = [transform_post(p) for p in posts]
    posts = [p for p in posts if filter_post(p)]
    rows = [get_row(p) for p in posts]
    convert_to_corpus(rows)


if __name__ == '__main__':
    raw_to_corpus()
