from os.path import join, dirname
from load_data import load_dataset
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.svm import SVC
from underthesea_flow.flow import Flow
from underthesea_flow.model import Model
from underthesea_flow.validation.validation import TrainTestSplitValidation

from experiment.category_svc.transformer import TfidfVectorizer

data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_category", "corpus", "data.xlsx")
X, y = load_dataset(data_file)


flow = Flow()

flow.data(X, y)

tranformer = TfidfVectorizer(ngram_range=(1, 4))
flow.transform(MultiLabelBinarizer())
flow.transform(tranformer)

classif = OneVsRestClassifier(SVC(kernel='linear'))
flow.add_model(Model(classif, name=SVC))

flow.set_validation(TrainTestSplitValidation(test_size=0.1))

flow.train()
flow.export_folder("model")
flow.export(model_name="SVC")
