import json
from os.path import join, dirname
from collections import OrderedDict
from underthesea.feature_engineering.text import Text
from underthesea.util.file_io import read
import pandas as pd
from underthesea.word_sent.regex_tokenize import tokenize
import re


file = join(dirname(__file__), "raw", "acts.json")
data = read(file)
posts = json.loads(data)
texts = [p["text"] for p in posts]


def multiple_replace(dict, text):
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


words_dict = {
    "khỏang": "khoảng",
    "tỏa": "toả",
    # "ìa": "ià"
}


def normalization(text):
    # remove special characters
    text = text.translate({ord(c): None for c in "\b"})
    # punctuation normalization
    text = multiple_replace(words_dict, text)
    return text


def analyze_tokens(texts):
    tokens = OrderedDict()
    for text in texts:
        tokens.update(get_tokens(text))
    df = pd.DataFrame(list(tokens.keys()))
    df.to_excel("tokens.xlsx")


def analyze_punctuation(texts):
    stats = {}
    for key in words_dict:
        stats[key] = 0
        for text in texts:
            if key in text:
                stats[key] += 1
    print(stats)


def detect(texts, pattern):
    for text in texts:
        text = normalization(text)
        tokens = set(tokenize(text).split())
        for token in tokens:
            if token == pattern:
                print(token)


def get_character_set(text):
    text = normalization(text)
    characters = set(text)
    return OrderedDict(((c, "") for c in characters))


def get_tokens(text):
    text = normalization(text)
    tokens = set(tokenize(text).split())
    return OrderedDict(((c, "") for c in tokens))


# characters = OrderedDict()
# for text in texts:
#     text = Text(text)
#     characters.update(get_character_set(text))
# df = pd.DataFrame(list(characters.keys()))
# df.to_excel("test.xlsx")
#


# for text in texts:
#     detect(text, "khỏang")
analyze_punctuation(texts)
detect(texts, "ìa")
texts = [normalization(text) for text in texts]
analyze_punctuation(texts)
analyze_tokens(texts)
print(0)
