from os.path import dirname, join

from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from underthesea_flow.flow import Flow
from underthesea_flow.model import Model
from underthesea_flow.transformer.tfidf import TfidfVectorizer
from underthesea_flow.validation.validation import TrainTestSplitValidation
from sklearn.preprocessing import MultiLabelBinarizer

from experiment.bank_2_logistic_unigrams.load_data import load_dataset

if __name__ == '__main__':
    data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_act_2", "corpus", "train.xlsx")
    X, y = load_dataset(data_file)

    flow = Flow()
    flow.log_folder = "log"

    flow.data(X, y)

    transformer = TfidfVectorizer()
    flow.transform(MultiLabelBinarizer())
    flow.transform(transformer)

    flow.add_model(Model(OneVsRestClassifier(LogisticRegression()), "LogisticRegression"))

    # flow.set_learning_curve(0.7, 1, 0.3)
    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    flow.train()

    flow.export_folder = "model"
    flow.export(model_name="LogisticRegression")