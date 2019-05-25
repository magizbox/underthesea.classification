from languageflow.data import Sentence
from languageflow.models.text_classifier import TextClassifier

model_folder = "tmp/classification_svm_vntc"
print(f"Load model from {model_folder}")
classifer = TextClassifier.load(model_folder)
print(f"Model is loaded.")


def predict(text):
    print(f"\nText: {text}")

    sentence = Sentence(text)
    classifer.predict(sentence)
    labels = sentence.labels
    print(f"Labels: {labels}")


predict('Huawei có thể không cần Google, nhưng sẽ ra sao nếu thiếu ARM ?')
predict('Trưởng phòng GD&ĐT xin lỗi vụ học sinh nhận khen thưởng là tờ giấy A4')
