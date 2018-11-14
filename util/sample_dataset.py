import argparse
import os
import shutil
from os.path import dirname, join, abspath
import pandas as pd

cwd = dirname(__file__)
root = dirname(cwd)

parser = argparse.ArgumentParser("sample_dataset.py")
parser.add_argument("--corpus", help="corpus path", required=True)
parser.add_argument("--sample", help="sample path", required=True)

args = parser.parse_args()

corpus_path = args.corpus
sample_path = args.sample

corpus_path = abspath(join(root, corpus_path))
sample_path = abspath(join(root, sample_path))

shutil.rmtree(sample_path, ignore_errors=True)
os.makedirs(sample_path, exist_ok=True)

train = pd.read_excel(join(corpus_path, "train.xlsx"))
test = pd.read_excel(join(corpus_path, "test.xlsx"))
n = 1000
train_sample = train.sample(n)
test_sample = test.sample(n)

train_sample.to_excel(join(sample_path, "train.xlsx"))
test_sample.to_excel(join(sample_path, "test.xlsx"))