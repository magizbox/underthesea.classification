from numpy import mean
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, f1_score, make_scorer
from sklearn.preprocessing import MultiLabelBinarizer
import time
import dill
from experiment.validation import TrainTestSplitValidation, CrossValidation
from models import save_model


class Experiment:
    def __init__(self, X, Y, clf, validation=None):
        self.clf = clf
        self.X = X
        self.Y = Y
        self.validation = validation

    def run(self):
        accuracy_scores = []
        f1_scores = []

        start = time.time()

        def score_func(y_true, y_pred, **kwargs):
            accuracy_scores.append(accuracy_score(y_true, y_pred, **kwargs))
            f1_scores.append(
                f1_score(y_true, y_pred, average='micro', **kwargs))

        try:
            scorer = make_scorer(score_func)
            if isinstance(self.validation, TrainTestSplitValidation):
                X_train, X_test, Y_train, Y_test = train_test_split(self.X,
                                                                    self.Y,
                                                                    test_size=self.validation.test_size)
                self.clf.fit(X_train, Y_train)
                Y_pred = self.clf.predict(X_test)
                score_func(Y_test, Y_pred)
            elif isinstance(self.validation, CrossValidation):
                cross_val_score(self.clf, self.X.toarray(), self.Y,
                                cv=self.validation.cv, scoring=scorer)
            f1 = mean(f1_scores)
            accuracy = mean(accuracy_scores)
            print("")
            print("F1: {:.4f}".format(f1))
            print(f1_scores)
            print("Accuracy: {:.4f}".format(accuracy))
            print(accuracy_scores)
            end = time.time()
            print("Running Time: {:.2f} seconds.".format(end - start))
        except Exception as e:
            raise (e)
            print("Error:", e)
            f1 = 0
            accuracy = 0
        return f1, accuracy

    def save(self, filename=None):
        self.clf.fit(self.X, self.Y, model_filename=filename)
