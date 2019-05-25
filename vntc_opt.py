import time
from tempfile import mkdtemp

from hyperopt import hp, Trials, fmin, tpe
from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import NLPData
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
from languageflow.trainers.model_trainer import ModelTrainer
from sacred import Experiment
from sacred.observers import MongoObserver
from sacred.optional import np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

ex = Experiment('vntc_opt')
ex.observers.append(MongoObserver.create())


@ex.main
def my_run(features__max_df, features__ngram_range):
    params = locals().copy()
    start = time.time()
    print(params)
    from languageflow.data_fetcher import DataFetcher
    corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.VNTC)
    pipeline = Pipeline(
        steps=[('features', TfidfVectorizer()),
               ('estimator', LinearSVC())
               ]
    )
    pipeline.set_params(**params)
    classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.PIPELINE, pipeline=pipeline)
    model_trainer = ModelTrainer(classifier, corpus)
    tmp_model_folder = mkdtemp()

    def micro_f1_score(y_true, y_pred):
        return f1_score(y_true, y_pred, average='micro')

    score = model_trainer.train(tmp_model_folder, scoring=micro_f1_score)
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
    'features__max_df': hp.choice('features__max_df', np.arange(0.5, 0.8, 0.1)),
    'features__ngram_range': hp.choice('features__ngram_range', [(1, 2), (1, 3)])
}

start = time.time()
trials = Trials()
best = fmin(objective, space=space, algo=tpe.suggest, max_evals=50, trials=trials)

print("Hyperopt search took %.2f seconds for 50 candidates" % ((time.time() - start)))
print(-best_score, best)
