import random

def sign(x):
    if x <= 0:
        return -1
    else:
        return 1


def generateXY():
    x = []
    for i in range(0, 20):
        x.append([random.random() * 2 - 1])
    noise = 0
    for i in range(0, 20):
        ran = random.random()
        if ran <= 0.2:
            noise += 1
            x[i].append(-sign(x[i][0]))
        else:
            x[i].append(sign(x[i][0]))
    return x


def decision_stump(dataset):
    sort_d = sorted(dataset)
    min_pos = []
    err = 0
    min_err = len(dataset)
    for i in range(0, len(dataset)+1):
        for k in range(0, i):
            if sort_d[k][1] > 0:
                err += 1
        for k in range(i, len(dataset)):
            if sort_d[k][1] < 0:
                err += 1
        if err < min_err:
            min_pos = [i]
            min_err = err
        elif err == min_err:
            min_pos.append(i)
        err = 0
    chosen = int(len(min_pos)*random.random())
    if min_pos[chosen] < len(sort_d):
        return [sort_d[min_pos[chosen]][0], min_err]
    else:
        return [(sort_d[min_pos[chosen]-1][0]+1) / 2, min_err]

def decision_stump_updated(dataset):
    sort_d = sorted(dataset)
    min_pos = []
    err = 0
    isNeg = False
    min_err = len(dataset)
    size = len(dataset)
    for i in range(0, len(dataset)+1):
        for k in range(0, i):
            if sort_d[k][1] > 0:
                err+=1
        for k in range(i, len(dataset)):
            if sort_d[k][1] < 0:
                err += 1
        isNeg = False
        if err < min_err:
            min_pos = []
            min_pos.append([i, isNeg])
            min_err = err
        elif err == min_err:
            min_pos.append([i, isNeg])
        isNeg = True
        if (size - err) < min_err:
            min_pos = []
            min_pos.append([i, isNeg])
            min_err = size - err

        elif (size - err) == min_err:
            min_pos.append([i, isNeg])
        err = 0
    choosen = int(len(min_pos) * random.random())
    if min_pos[choosen][0] < len(sort_d):
        return [sort_d[min_pos[choosen][0]][0], min_err, min_pos[choosen][1]]
    else:
        return [(sort_d[min_pos[choosen][0]-1][0]+1) / 2, min_err, min_pos[choosen][1]]

    def multiDDecision_stump(dataset):
        min_err_d = []
        min_err = 0x7fffffff
        err = 0
        for i in range(len(dataset)):  #
            temp = decision_stump(dataset[i])
            err = temp[1]
            # print(err)
            if err < min_err:
                min_err = err
                min_err_d = []
                min_err_d.append([temp[0], i, min_err, temp[2]])

            elif err == min_err:
                min_err_d.append([temp[0], i, min_err, temp[2]])
        choosen = int(random.random() * len(min_err_d))
        return min_err_d[choosen]

def multiDDecision_stump(dataset):
    min_err_d = []
    min_err = 0x7fffffff
    err = 0
    for i in range(len(dataset)):
        temp = decision_stump(dataset[i])
        err = temp[1]
        if err < min_err:
            min_err = err
            min_err_d = []
            min_err_d.append([temp[0], i, min_err,temp[2]])
        elif err == min_err:
            min_err_d.append([temp[0], i, min_err,temp[2]])
    choosen = int(random.random() * len(min_err_d))
    return min_err_d[choosen]

def readDataFrom(filename):
    result = []
    with open (filename) as f:
        line = f.readline()[1:-1]
        while line:
            temp = line.split(' ')
            if len(result) == 0:
                for x_i in range(len(temp)-1):
                    result.append([[float(temp[x_i]), float(temp[-1])]])
            else:
                for x_i in range(len(temp) - 1):
                    result[x_i].append([float(temp[x_i]), float(temp[-1])])
            line = f.readline()[1:-1]
    return result

def checkout(min_err_d, dataset):
    err = 0
    for i in dataset[min_err_d[1]]:
        if sign(i[0] - min_err_d[0]) != sign(i[1]):
            err += 1
    if min_err_d[3] == True:
        err = len(dataset[0]) - err
    return err