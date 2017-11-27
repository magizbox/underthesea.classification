from os.path import join, dirname
import json
import pandas as pd

from underthesea.util.file_io import read


def filter_post(post):
    meta = post["meta"]
    return meta["from_id"] != meta["target_id"]


def transform_post(post):
    post["meta"] = json.loads(post["meta"])
    post["act"] = json.loads(post["act"])
    post["act"] = [act["name"] for act in post["act"]]
    return post


def get_row(post):
    row = {}
    row["text"] = post["text"]
    row["labels"] = post["act"]
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
    file = join(dirname(__file__), "corpus", "data.xlsx")
    columns = ["text"] + labels
    df.to_excel(file, index=False, columns=columns)
    pass


def raw_to_corpus():
    file = join(dirname(__file__), "raw", "posts_act.json")
    data = read(file)
    posts = json.loads(data)
    posts = [transform_post(p) for p in posts]
    posts = [p for p in posts if filter_post(p)]
    rows = [get_row(p) for p in posts]
    convert_to_corpus(rows)


if __name__ == '__main__':
    raw_to_corpus()
