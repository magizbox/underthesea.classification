from os.path import join
import pandas as pd
from underthesea.util.file_io import read


def to_excel(model):
    lines = read(model).strip().split("\n")
    content = [line.split(":")[1] for line in lines]
    return content


if __name__ == '__main__':
    x_category_1_svm_ngrams = join("x_category_1_svm_ngrams", "log", "result.txt")
    category_naive_bayes_multinomialNB = join("category_naive_bayes_multinomialNB", "log", "result.txt")
    category_naive_bayes_gaussianNB = join("category_naive_bayes_gaussianNB", "log", "result.txt")
    category_naive_bayes_bernoulliNB = join("category_naive_bayes_bernoulliNB", "log", "result.txt")

    labels = ['X Shape', 'Train', 'Test', 'Accuracy ', 'F1 (micro) ', 'F1 (macro) ', 'F1 (weighted)', 'Running Time']
    models = ['', 'x_category_1_svm_ngrams', 'category_naive_bayes_bernoulliNB', "category_naive_bayes_multinomialNB"]
    model = [item for item in models]
    content = [labels, to_excel(x_category_1_svm_ngrams), to_excel(category_naive_bayes_bernoulliNB),
               to_excel(category_naive_bayes_multinomialNB)]

    df = pd.DataFrame(content, model)
    df.to_excel("models.xlsx", header=None)
