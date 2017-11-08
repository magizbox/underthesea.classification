from os.path import join, dirname
import json
import pandas as pd

from underthesea.util.file_io import read


def filter_post(post):
    if len(post["category"]) > 0:
        return True
    else:
        return False


def transform_post(post):
    post["meta"] = json.loads(post["meta"])
    try:
        post["category"] = json.loads(post["category"])
    except:
        post["category"] = []
    post["category"] = list(
        set([item["name"] for item in post["category"] if item["name"]]))
    return post


def get_row(post):
    row = {}
    row["text"] = post["text"]
    row["labels"] = post["category"]
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
    file = join(dirname(__file__), "raw", "categories.json")
    data = read(file)
    posts = json.loads(data)
    posts = [transform_post(p) for p in posts]
    posts = [p for p in posts if filter_post(p)]
    rows = [get_row(p) for p in posts]
    convert_to_corpus(rows)


if __name__ == '__main__':
    raw_to_corpus()
