import numpy as np
import numpy.linalg as la

def cost_function(weights, features, labels):
    return np.power(np.dot(features, weights) - labels, 2) / weights.shape[0]

def training(features, labels):
    """
    :param features: a m x n matrix where m is the number of features and n is the number of inputs.
    :param labels: a n x 1 vector where n is the number of ouputs.
    :return: the optimal weights of the linear regression.
    """
    pseudo_inverse = la.pinv(features)
    weights = np.dot(pseudo_inverse, labels)
    return weights


