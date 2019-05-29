import random
import time
from os import listdir, remove

from hyperopt import hp, Trials, fmin, tpe
from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sacred import Experiment
from sacred.observers import MongoObserver
from sacred.optional import np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import LinearSVC
from text_features import Tokenize

from text_features import Lowercase

ex = Experiment('vntc_opt_29')
ex.observers.append(MongoObserver.create())


@ex.main
def my_run(features__lower_pipe__tfidf__max_df,
           features__lower_pipe__tfidf__ngram_range,
           features__with_tone_char__ngram_range,
           features__lower_pipe__tfidf__max_features,
           features__with_tone_char__max_features):
    params = locals().copy()
    start = time.time()
    print(params)
    corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.VNTC)
    pipeline = Pipeline(
        steps=[
            ('features', FeatureUnion([
                ('lower_pipe', Pipeline([
                    ('tokenize', Tokenize()),
                    ('lower', Lowercase()),
                    ('tfidf', TfidfVectorizer(ngram_range=(1, 4)))])),
                ('with_tone_char', TfidfVectorizer(ngram_range=(1, 6), analyzer='char'))])),
            ('estimator', LinearSVC())
        ]
    )
    pipeline.set_params(**params)
    classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
    model_trainer = ModelTrainer(classifier, corpus)
    tmp_model_folder = "tmp/tmp_model"

    def micro_f1_score(y_true, y_pred):
        return f1_score(y_true, y_pred, average='micro')

    score = model_trainer.train(tmp_model_folder, scoring=micro_f1_score)
    tmp_files = listdir(tmp_model_folder)
    for file in tmp_files:
        if "gitignore" in file:
            continue
        remove(f"{tmp_model_folder}/{file}")
    ex.log_scalar('dev_score', score['dev_score'])
    ex.log_scalar('test_score', score['test_score'])
    print(time.time() - start)
    return score['dev_score']


best_score = 1.0


def objective(space):
    global best_score
    test_score = ex.run(config_updates=space).result
    score = 1 - test_score
    print("Score:", score)
    return score


space = {
    'features__lower_pipe__tfidf__max_df': hp.choice('features__lower_pipe__tfidf__max_df', np.arange(0.5, 0.8, 0.1)),
    'features__lower_pipe__tfidf__max_features': hp.choice('features__lower_pipe__tfidf__max_features',
                                                           np.arange(5000, 30000, 1000)),
    'features__lower_pipe__tfidf__ngram_range': hp.choice('features__lower_pipe__tfidf__ngram_range',
                                                          [(1, 3), (1, 4)]),
    'features__with_tone_char__ngram_range': hp.choice('features__with_tone_char__ngram_range',
                                                       [(1, 3), (1, 4)]),
    'features__with_tone_char__max_features': hp.choice('features__with_tone_char__max_features',
                                                        np.arange(5000, 30000, 1000)),
}

start = time.time()
trials = Trials()
best = fmin(objective, space=space, algo=tpe.suggest, max_evals=200, trials=trials)

print(f"Hyperopt search took {round((time.time() - start), 2)} seconds for 200 candidates")
print(-best_score, best)
