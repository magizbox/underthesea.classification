import pickle

filename = "fasttext.model"
clf = pickle.load(open(filename, "rb"))
print(0)