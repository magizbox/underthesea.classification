import os
import shutil
import time

from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC

from text_features import Lowercase, RemoveTone, CountEmoticons

model_folder = "tmp/classification_svm_uts2017_bank"
try:
    shutil.rmtree(model_folder)
except:
    pass
finally:
    os.makedirs(model_folder)

lower__ngram_range = (1, 3)
with_tone__ngram_range = (1, 4)
remove_tone__ngram_range = (1, 4)
count__max_features = 4000
estimator__C = 0.75

start = time.time()
print(">>> Train UTS2017_BANK Classification")
corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.UTS2017_BANK_TC)
print("\n\n>>> Sample sentences")
for s in corpus.train[:10]:
    print(s)
pipeline = Pipeline(
    steps=[
        ('features', FeatureUnion([
            ('lower_pipe', Pipeline([
                ('lower', Lowercase()),
                ('tfidf', TfidfVectorizer(ngram_range=lower__ngram_range, norm='l2', min_df=2, max_features=count__max_features))])),
            ('with_tone_char', TfidfVectorizer(ngram_range=with_tone__ngram_range, norm='l2', min_df=2, analyzer='char')),
            ('remove_tone', Pipeline([
                ('remove_tone', RemoveTone()),
                ('lower', Lowercase()),
                ('tfidf', TfidfVectorizer(ngram_range=remove_tone__ngram_range, norm='l2', min_df=2))])),
            ('emoticons', CountEmoticons())
        ])),
        ('estimator', SVC(kernel='linear', C=estimator__C, class_weight=None, verbose=True))
    ]
)
classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
model_trainer = ModelTrainer(classifier, corpus)


def micro_f1_score(y_true, y_pred):
    return f1_score(y_true, y_pred, average='micro')


model_trainer.train(model_folder, scoring=micro_f1_score)
print(f"\n\n>>> Finish training in {round(time.time() - start, 2)} seconds")
print(f"Your model is saved in {model_folder}")
