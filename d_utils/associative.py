import numpy as np, csv

def load_matrix(filename):
    labels = []
    data = []
    with open(filename) as file:
        csvinput = csv.reader(file, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)

        for row in csvinput:
            labels.append(row[0])
            data.append(row[1:])

        data = data[2:]
        mod = labels[0]
        labels = labels[2:]
    return mod, labels, data

def is_associative(labels, matrix):
    return False
