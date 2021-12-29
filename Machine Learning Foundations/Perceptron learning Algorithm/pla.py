import numpy as np
import pandas as pd


def preprocess(path):
    dataset = pd.read_csv(path, names=['x1', 'x2', 'x3', 'x4', 'y'], delim_whitespace=True)
    dataset.insert(0, 'x0', 1)
    training_set = dataset.iloc[:, :-1].values
    labels_set = dataset.iloc[:, -1].values
    return training_set, labels_set


def sign(x):
    if x <= 0:
        return -1
    else:
        return 1


def pla(training_set, labels_set):
    update_count = 0
    correct_count = 0
    weights = np.zeros(training_set.shape[1])
    converge = False
    while not converge:
        for i in range(training_set.shape[0]):
            x = training_set[i]
            y = labels_set[i]
            if sign(np.dot(weights, x)) != y:
                weights = weights + y * x
                update_count += 1
                correct_count = 0
            else:
                correct_count += 1
                if correct_count == labels_set.shape[0]:
                    converge = True
                    break
    return weights, update_count


training_set, labels_set = preprocess("train.dat")
weights, count = pla(training_set, labels_set)
print("Number of Updates:", count)


def unison_shuffled_copies(arr1, arr2):
    assert len(arr1) == len(arr2)
    p = np.random.permutation(len(arr1))
    return arr1[p], arr2[p]

def pla_random(training_set, labels_set, times_repeat):
    total = 0
    for _ in range(times_repeat):
        xs, ys = unison_shuffled_copies(training_set, labels_set)
        _, count = pla(xs, ys)
        total += count
    return total / times_repeat

avg = pla_random(training_set, labels_set, 2000)
print(f"Average Number of Updates in 2000 Experiments:", avg)


def error_counter(wt, xs, ys):
    count = 0
    for i in range(len(xs)):
        if sign(np.dot(wt, xs[i])) != ys[i]:
            count += 1
    return count




def pocket_pla(training_set, labels_set, time_repeat):
    weights = np.zeros(training_set.shape[1])
    weights_updated = weights.copy()
    error = error_counter(weights, training_set, labels_set)
    t = 0
    while t < time_repeat:
        i = np.random.randint(0, len(training_set))
        if sign(np.dot(weights, training_set[i])) != labels_set[i]:
            weights += training_set[i] * labels_set[i]
            new_error = error_counter(weights, training_set, labels_set)
            t += 1
            if new_error < error:
                weights_updated = weights.copy()
                error = new_error
    return weights_updated


training_set_new, labels_set_new = preprocess("train18.dat")
weights = pocket_pla(training_set_new, labels_set_new, 50)

testing_set, testing_label_set = preprocess("test.dat")

def pocket_test(weights, testing_set, testing_label_set):
    err_cnt = error_counter(weights, testing_set, testing_label_set)
    err_rate = err_cnt / len(testing_set)
    return err_rate

error_rate = pocket_test(weights, testing_set, testing_label_set)
print(f"The error rate is {error_rate}.")