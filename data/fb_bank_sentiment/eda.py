import pandas as pd
import matplotlib.pyplot as plt
from os.path import join
from pylab import rcParams


def analyze(input, name):
    input = "corpus/" + input
    df = pd.read_excel(input, encoding='sys.getfilesystemencoding()')
    print("Dataset '{}' is loaded!".format(name))
    print("\t- size:", df.shape)
    rcParams['figure.figsize'] = 13, 6
    df.drop("text", axis=1).sum().plot.barh()
    plt.savefig(join(output_folder, "{}_labels_distribution.png".format(name)))
    plt.clf()


output_folder = "eda/"
analyze("data.xlsx", "data")
analyze("train.xlsx", "train")
analyze("test.xlsx", "test")
