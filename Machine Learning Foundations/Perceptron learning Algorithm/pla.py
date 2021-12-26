import numpy as np


def sign(x, w):
    """
    :param x: the input xs of the linear classifier.
    :param w: the weighs of the linear classifier.
    :return: True if the sign of the inner dot product is positive.
    """
    return np.dot(x, w) >= 0


def pla_linear_separable(training_samples, ys):
    """
    Perceptron learning algorithm when linear separable.
    :param training_samples: a matrix which rows are training data of inputs and columns are each features.
    :param ys: a numpy array containing the expected output of the training samples.
    :return: a numpy array as a vector contains all weights that best approximate the linear classifier.
    """
    weights = np.zeros(training_samples.shape[1])
    for i in range(training_samples.shape[0]):
        x = training_samples[i]
        if sign(x, weights) != ys[i]:
            # find a mistake, the weights need to be adjusted.
            weights = weights + ys[i] * x
    return weights


def mistaken_count(training_samples, ys, w):
    """
    :param training_samples: a matrix which rows are training data of inputs and columns are each features.
    :param ys: a numpy array containing the expected output of the training samples.
    :param w: the weighs of the linear classifier.
    :return: the number of mistakes that w have made.
    """
    count = 0
    for i in range(training_samples.shape[0]):
        x = training_samples[i]
        if sign(x, w) != ys[i]:
            count += 1
    return count


def pla_linear_non_separable(training_samples, ys, number_iter):
    """
    Perceptron learning algorithm when linear non-separable.
    :param training_samples: a matrix which rows are training data of inputs and columns are each features.
    :param ys: a numpy array containing the expected output of the training samples.
    :return: a numpy array as a vector contains all weights that best approximate the linear classifier.
    """
    weights = np.zeros(training_samples.shape[1])
    count = mistaken_count(training_samples, ys, weights)
    while number_iter:
        for i in range(training_samples.shape[0]):
            x = training_samples[i]
            if sign(x, weights) != ys[i]:
                _weights = weights + ys[i] * x
                _count = mistaken_count(training_samples, ys, _weights)
                if _count < count:
                    weights = _weights
                    count = _count
        number_iter -= 1
    return weights
