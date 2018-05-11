import pandas as pd
import pickle

from os.path import join
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from underthesea.dictionary import Dictionary
from underthesea.feature_engineering.text import Text
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, NuSVC, LinearSVC

from experiment.flow import Flow, Model
from experiment.transformer import TfidfVectorizer, TfidfDictionaryVectorizer

from experiment.validation import TrainTestSplitValidation, CrossValidation
from model.model_fasttext import FastTextClassifier, FastTextPredictor


def load_dataset(data_file):
    df = pd.read_excel(data_file)
    X = list(df["text"])

    def convert_text(x):
        try:
            return Text(x)
        except:
            pass
        return ""

    X = [convert_text(x) for x in X]
    y = df.drop("text", 1)
    # labels = Y.columns
    columns = y.columns
    temp = y.apply(lambda _: _ > 0)
    y = list(temp.apply(lambda _: list(columns[_.values]), axis=1))
    return X, y


if __name__ == '__main__':
    # data_file = "corpus/data_3k.xlsx"
    # data_file = "corpus/data_10k.xlsx"
    data_file = "corpus/data.xlsx"
    X, y = load_dataset(data_file)

    flow = Flow()

    flow.data(X, y)

    # transformer = TfidfVectorizer()
    # dictionary = Dictionary.Instance()
    # vocabulary = list(dictionary.words.keys())
    # transformer = TfidfVectorizer(ngram_range=(1, 2), max_features=4000)
    # transformer = TfidfVectorizer(ngram_range=(1, 3), max_features=4000)
    # transformer = TfidfVectorizer(default_vocabulary=vocabulary, ngram_range=(1, 3), max_features=4000)
    # transformer = TfidfDictionaryVectorizer(default_vocabulary=vocabulary, ngram_range=(1, 3), max_features=4000)
    # transformer = TfidfVectorizer(tokenizer=tokenize)
    # flow.transform(transformer)

    # flow.add_model(Model(GaussianNB(), "GaussianNB"))
    # flow.add_model(Model(LinearSVC(), "LinearSVC"))

    # flow.add_model(Model(OneVsRestClassifier(GaussianNB()), "GaussianNB"))
    # flow.add_model(Model(OneVsRestClassifier(NuSVC(nu=0.99)), "NuSVC"))
    # flow.add_model(Model(OneVsRestClassifier(SVC()), "SVC"))
    # flow.add_model(Model(OneVsRestClassifier(XGBClassifier(nthread=8)), "XGBoost"))
    # flow.add_model(Model(OneVsRestClassifier(FastTextClassifier()), "FastText"))
    flow.add_model(Model(FastTextClassifier(), "FastText"))

    # flow.set_learning_curve(0.7, 1, 0.3)

    flow.set_validation(TrainTestSplitValidation(test_size=0.1))
    # flow.set_validation(CrossValidation(cv=5))

    # flow.validation()

    # model_name = "GaussianNB"
    # model_name = "FastText"
    # model_filename = join("results", "fasttext", "fasttext.model")
    # flow.save_model(model_name="FastText", model_filename=model_filename)

    model = FastTextPredictor.Instance()
    X_test, y_test = X, y
    flow.test(X_test, y_test, model)
