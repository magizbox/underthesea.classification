from os import listdir, makedirs
from os.path import dirname, join, exists

ROOT_FOLDER = dirname(dirname(dirname(__file__)))
RAW_FOLDER = join(ROOT_FOLDER, "data", "vntc", "raw")
TRAIN_RAW_FOLDER = join(RAW_FOLDER, "Train_Full")
categories = listdir(TRAIN_RAW_FOLDER)
TEST_RAW_FOLDER = join(RAW_FOLDER, "Test_Full")
DATA_FOLDER = join(dirname(__file__), "data")
trainpath = join(DATA_FOLDER, "train")
testpath = join (DATA_FOLDER, "test")

if not exists(trainpath):
    makedirs(trainpath)
if not exists(testpath):
    makedirs(testpath)

for category in categories[:2]:
    category_path = join(trainpath, f"{category}.txt")
    category_file = open(category_path, "a")
    for file in listdir(join(TRAIN_RAW_FOLDER, category)):
        filepath = join(TRAIN_RAW_FOLDER, category, file)
        content = open(filepath, "rb").read().decode("utf-16")
        category_file.write(content)

for category in listdir(TEST_RAW_FOLDER)[:2]:
    category_path = join(testpath, category)
    if not exists(category_path):
        makedirs(category_path)
    for file in listdir(join(TEST_RAW_FOLDER, category))[:10]:
        filepath = join(TEST_RAW_FOLDER, category, file)
        content = open(filepath, "rb").read().decode("utf-16")
        output_file = open(join(category_path, file), "w")
        output_file.write(content)



