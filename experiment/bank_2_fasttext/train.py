from os.path import dirname, join
from underthesea_flow.flow import Flow
from underthesea_flow.model import Model
from underthesea_flow.validation.validation import TrainTestSplitValidation

from load_data import load_dataset
from model.model_fasttext import FastTextClassifier

if __name__ == '__main__':
    data_file = join(dirname(dirname(dirname(dirname(__file__)))), "data", "fb_bank_act_2", "corpus", "data.xlsx")
    X, y = load_dataset(data_file)

    flow = Flow()
    flow.log_folder = "log"

    flow.data(X, y)

    flow.add_model(Model(FastTextClassifier(), "FastText"))

    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    # flow.validation()

    model_name = "FastText"
    model_filename = join("model", "fasttext.model")
    flow.train()
    flow.save_model(model_name="FastText", model_filename=model_filename)