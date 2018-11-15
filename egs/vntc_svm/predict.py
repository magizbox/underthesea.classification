from os.path import dirname, join
import pickle

cwd = dirname(__file__)
x_transformer_file = open(join(cwd, "snapshots", "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)

y_transformer_file = open(join(cwd, "snapshots", "y_transformer.pkl"), "rb")
y_transformer = pickle.load(y_transformer_file)

estimator_file = open(join(cwd, "snapshots", "model.pkl"), "rb")
estimator = pickle.load(estimator_file)

def classify(text):
    X = x_transformer.transform([text])
    y = estimator.predict(X)
    label = y_transformer.inverse_transform(y)
    return label

text = "Theo nguồn tin của Dân trí, Tập đoàn Hoá chất (Vinachem) vừa báo cáo, do tình hình tài chính của Tập đoàn hiện nay rất khó khăn nên không có đủ khả năng thu xếp nguồn tiền để trả nợ toàn bộ các khoản vay đến hạn cho Ngân hàng Phát triển Việt Nam trong năm 2018"
label = classify(text)
print(label)