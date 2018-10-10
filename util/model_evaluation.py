import itertools

import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt


def get_metrics(true_labels, predicted_labels):
    print('Accuracy:', np.round(
        metrics.accuracy_score(true_labels,
                               predicted_labels),
        3))
    print('Precision:', np.round(
        metrics.precision_score(true_labels,
                                predicted_labels,
                                average='weighted'),
        3))
    print('Recall:', np.round(
        metrics.recall_score(true_labels,
                             predicted_labels,
                             average='weighted'),
        3))
    print('F1 Score:', np.round(
        metrics.f1_score(true_labels,
                         predicted_labels,
                         average='weighted'),
        3))


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
