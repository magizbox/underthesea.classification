import eli5
from eli5.lime import TextExplainer
from os.path import join, dirname

from load_data import load_dataset

from model import predict_proba

data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_category",
                 "corpus", "test.xlsx")
X_test, y_test = load_dataset(data_file)
doc = X_test[0]

te = TextExplainer(random_state=42)
te.fit(doc, predict_proba)
te.show_prediction()
print(0)