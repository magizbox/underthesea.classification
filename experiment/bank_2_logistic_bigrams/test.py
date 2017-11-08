from os.path import join, dirname
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import json

from underthesea.util.file_io import write

from load_data import load_dataset
from model.model import predict
from sklearn.metrics import confusion_matrix

data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_act_2",
                 "corpus", "test.xlsx")
X_test, y_test = load_dataset(data_file)
y_test = [tuple(item) for item in y_test]
y_pred = predict(X_test)


def accuracy_score(TP, FP, TN, FN):
    return round((TP + TN) / (TP + FP + TN + FN), 2)


def precision_score(TP, FP, TN, FN):
    try:
        return round(TP / (TP + FP), 2)
    except:
        return 0


def recall_score(TP, FP, TN, FN):
    try:
        return round(TP / (TP + FN), 2)
    except:
        return 0


def f1_score(TP, FP, TN, FN):
    p = precision_score(TP, FP, TN, FN)
    r = recall_score(TP, FP, TN, FN)
    try:
        f1 = round((2 * p * r) / (p + r), 2)
    except:
        f1 = 0
    return f1


# generate score
labels = set(sum(y_test + y_pred, ()))
score = {}
for label in labels:
    score[label] = {}
    TP, FP, TN, FN = (0, 0, 0, 0)

    for i in range(len(y_test)):
        if label in y_test[i]:
            if label in y_pred[i]:
                TP += 1
            else:
                FN += 1
        else:
            if label in y_pred[i]:
                FP += 1
            else:
                TN += 1
    score[label] = {
        "TP": TP,
        "FP": FP,
        "TN": TN,
        "FN": FN,
        "accuracy": accuracy_score(TP, FP, TN, FN),
        "precision": precision_score(TP, FP, TN, FN),
        "recall": recall_score(TP, FP, TN, FN),
        "f1": f1_score(TP, FP, TN, FN),
    }

df = pd.DataFrame.from_dict(score)
df.T.to_excel("inspect/score.xlsx", columns=["TP", "TN", "FP", "FN", "accuracy", "precision", "recall", "f1"])

# generate result
result = {
    "X_test": X_test,
    "y_test": y_test,
    "y_pred": y_pred,
    "score": score
}

content = json.dumps(result, ensure_ascii=False)
write("inspect/result.json", content)
