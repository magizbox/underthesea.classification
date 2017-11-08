from os.path import dirname, join
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from underthesea_flow.flow import Flow
from underthesea_flow.model import Model
from underthesea_flow.validation.validation import TrainTestSplitValidation
from sklearn.preprocessing import MultiLabelBinarizer
from load_data import load_dataset
from transformer import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
if __name__ == '__main__':
    data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_category", "corpus", "train.xlsx")
    X, y = load_dataset(data_file)

    flow = Flow()
    flow.log_folder = "log"

    flow.data(X, y)

    transformer = TfidfVectorizer(ngram_range=(1, 3))
    flow.transform(MultiLabelBinarizer())
    flow.transform(transformer)

    flow.add_model(Model(OneVsRestClassifier(SGDClassifier(loss='log')), "SGD"))

    # flow.set_learning_curve(0.7, 1, 0.3)
    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    flow.train()
    flow.export_folder = "model"
    flow.export(model_name="SGD")