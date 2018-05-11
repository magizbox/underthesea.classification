import numpy
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

from util.experiment.experiment import Experiment
from experiment.validation import TrainTestSplitValidation


class Model:
    def __init__(self, clf, name):
        self.clf = clf
        self.name = name


class Flow:
    def __init__(self):
        self.models = []
        self.lc_range = [1]
        self.result = []
        self.validation = TrainTestSplitValidation()

    def data(self, X, Y):
        self.X = X
        self.Y = Y

    def transform(self, transformer):
        self.X = transformer.text2vec(self.X).toarray()
        print("X Shape: ", self.X.shape)
        # transformer.save()

    def add_model(self, model):
        self.models.append(model)

    def set_learning_curve(self, start, stop, offset):
        self.lc_range = numpy.arange(start, stop, offset)

    def set_validation(self, validation):
        self.validation = validation

    def validation(self):
        colors = ['red', 'green', 'yellow', 'blue']
        legends = []

        # fig, ax = plt.subplots(figsize=(10, 6))
        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        for i, model in enumerate(self.models):
            f1_scores = []
            accuracy_scores = []
            N = [int(i * len(self.Y)) for i in self.lc_range]
            for n in N:
                X = self.X[:n]
                Y = self.Y[:n]
                e = Experiment(X, Y, model.clf, self.validation)
                f1, accuracy = e.run()
                f1_scores.append(f1)
                accuracy_scores.append(accuracy)
            # plt.gca().set_color_cycle([colors[i], colors[i]])
            # plt.plot(N, f1_scores, ls='solid')
            # plt.plot(N, accuracy_scores, ls='dotted')
            legends.append("{} f1".format(model.name))
            legends.append("{} accuracy".format(model.name))
            # ax.legend(legends, loc='center left', bbox_to_anchor=(1, 0.5))
            # plt.xlabel("Train size")
            # plt.ylabel("Score")
            # plt.savefig("learning_curve.png")
            # plt.show()

    def visualize(self):
        pass

    def train(self):
        """
        Train dataset with transformer and model
        """
        pass

    def save_model(self, model_name, model_filename):
        model = [model for model in self.models if model.name == model_name][0]
        e = Experiment(self.X, self.Y, model.clf, None)
        e.save(model_filename)

    def test(self, X, y_true, model):
        y_predict = model.predict(X)
        y_true = [item[0] for item in y_true]
        print(accuracy_score(y_true, y_predict))
