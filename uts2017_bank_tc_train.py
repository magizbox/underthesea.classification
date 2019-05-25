import os
import shutil
import time

from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

model_folder = "tmp/classification_svm_uts2017_bank"
try:
    shutil.rmtree(model_folder)
except:
    pass
finally:
    os.makedirs(model_folder)

count__ngram_range = (1, 3)
count__max_features = 4000
estimator__C = 0.3

start = time.time()
print(">>> Train UTS2017_BANK Classification")
corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.UTS2017_BANK_TC)
print("\n\n>>> Sample sentences")
for s in corpus.train[:10]:
    print(s)
pipeline = Pipeline(
    steps=[('features', CountVectorizer(ngram_range=count__ngram_range, max_features=count__max_features)),
           ('estimator', SVC(kernel='linear', C=estimator__C))]
)
classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
model_trainer = ModelTrainer(classifier, corpus)


def macro_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')


model_trainer.train(model_folder, scoring=macro_f1_score)
print(f"\n\n>>> Finish training in {round(time.time() - start, 2)} seconds")
print(f"Your model is saved in {model_folder}")
