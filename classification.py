import argparse
import os
import pickle
from os.path import dirname, join

from util.load_data import normalize_text

parser = argparse.ArgumentParser("classification.py")
text = parser.add_argument_group("The following arguments are mandatory for text option")
text.add_argument("--text", metavar="TEXT", help="text to predict", nargs="?")
args = parser.parse_args()


path = join(dirname(__file__), "models")
models = [i for i in os.listdir(path) if i.endswith(".pkl")]
if len(models) == 0:
    print("Download default model.....")
    os.system("sh util/get_default_model.sh")
    print("Done!!!\n")

x_transformer_file = open(join(path, "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)

y_transformer_file = open(join(path, "y_transformer.pkl"), "rb")
y_transformer = pickle.load(y_transformer_file)

ch2_file = open(join(path, "ch2.pkl"), "rb")
ch2 = pickle.load(ch2_file)

estimator_file = open(join(path, "model.pkl"), "rb")
estimator = pickle.load(estimator_file)

if not args.text:
    parser.print_help()

if args.text:
    text = args.text
    text = normalize_text(text)
    X = x_transformer.transform([text])
    X = ch2.transform(X)
    y = estimator.predict(X)
    label = y_transformer.inverse_transform(y)[0]
    print("Label: ", label)
