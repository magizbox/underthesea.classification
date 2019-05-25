from languageflow.data import Sentence
from languageflow.models.text_classifier import TextClassifier

model_folder = "tmp/classification_svm_uts2017_bank"
print(f"Load model from {model_folder}")
classifer = TextClassifier.load(model_folder)
print(f"Model is loaded.")


def predict(text):
    print(f"\nText: {text}")

    sentence = Sentence(text)
    classifer.predict(sentence)
    labels = sentence.labels
    print(f"Labels: {labels}")


predict('Tôi rất ấn tượng với VPBank ở khoản này, mọi thứ đều là rất nhanh')
predict('có lẽ web online của BIDV đáng bị âm điểm')
