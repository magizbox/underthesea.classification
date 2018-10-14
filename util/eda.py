from os.path import dirname, join

import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt


def analyze(path, name):
    df = pd.read_excel(path)
    print("Dataset {} is loaded".format(name))
    print("\t - size", df.shape)
    rcParams['figure.figsize'] = 13, 6
    df.drop("text", axis=1).sum().sort_values().plot.barh()
    plt.savefig(join(folder, "eda", "{}_labels_distribution.png".format(name)))
    plt.clf()


folder = join(dirname(dirname(__file__)), "data")
analyze(join(folder, "corpus", "train.xlsx"), "train")
analyze(join(folder, "corpus", "test.xlsx"), "test")

