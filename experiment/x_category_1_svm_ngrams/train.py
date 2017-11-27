from os.path import dirname, join
from languageflow.flow import Flow
from languageflow.model import Model
from languageflow.transformer.tfidf import TfidfVectorizer
from languageflow.validation.validation import TrainTestSplitValidation
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from load_data import load_dataset
from sklearn.linear_model import SGDClassifier

if __name__ == '__main__':
    data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_category", "corpus", "train.xlsx")
    X, y = load_dataset(data_file)
    # n = 30
    # X, y = X[:n], y[:n]
    flow = Flow()
    flow.log_folder = "log"

    flow.data(X, y)

    transformer = TfidfVectorizer(ngram_range=(1, 3))
    flow.transform(MultiLabelBinarizer())
    flow.transform(transformer)

    flow.add_model(Model(OneVsRestClassifier(SGDClassifier()), "SGD"))

    # flow.set_learning_curve(0.7, 1, 0.3)
    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    flow.train()
    flow.export(model_name="SGD", export_folder="model")
