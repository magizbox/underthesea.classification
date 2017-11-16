import json
from os.path import join, dirname
import pandas as pd
from underthesea.util.file_io import read


def fillter_post(post):
    if "\b" in post["text"]:
        return False
    if len(post["act"]) > 0:
        return True
    else:
        return False


def transform_posts(post):
    # post["meta"] = json.loads(post["meta"])
    post["act"] = json.loads(post["act"])
    post["act"] = list(set([act["name"] for act in post["act"] if act["name"]]))
    return post


def get_row(post):
    row = {}
    row["text"] = post["text"]
    row["labels"] = post["act"]
    return row


def to_excel(rows):
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
    size = 0.8
    split = int(size * n)
    train_file = join(dirname(__file__), "corpus", "train.xlsx")
    test_file = join(dirname(__file__), "corpus", "test.xlsx")
    data_file = join(dirname(__file__), "corpus", "data.xlsx")
    columns = ["text"] + labels
    df.ix[:split, :].to_excel(train_file, index=False, columns=columns)
    df.ix[split:, :].to_excel(test_file, index=False, columns=columns)
    df.to_excel(data_file, index=False, columns=columns)


if __name__ == '__main__':
    data_file = join(dirname(__file__), "raw", "acts.json")
    content = read(data_file)
    data = json.loads(content)
    posts = [transform_posts(post) for post in data]
    posts = [p for p in posts if fillter_post(p)]
    rows = [get_row(p) for p in posts]
    to_excel(rows)
