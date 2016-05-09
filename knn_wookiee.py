import numpy as np

def distance(x1,x2):
    x1 = np.array(x1)
    x2 = np.array(x2)
    return np.linalg.norm(x1-x2)


def cool_function(X_train,y_train,X_test):
    arr_train = np.array(X_train)
    index=np.zeros(len(X_test))
    for j,vector in enumerate(X_test):
        dist = np.zeros(len(X_train))
        arr_test = np.array(vector)
        for i,vect in enumerate(X_train):
            arr = np.array(vect)
            dist[i] = distance_arr(arr,arr_test)
        index[j] = np.argmin(dist)
    for l in index:
        print y_train[l.astype(int)]


X_train = [[1,   1,  1],
           [0,   0,  0],
           [-1, -1, -1],
           [10, 10, 10]]

y_train = ['red',
           'white',
           'blue',
           'chartreuse']

X_test = [[1.1, 1.1, 1.1]]


# -- solution --

def oneNN(X_train, y_train, X_test):
    for test in X_test:
        index, point = min(enumerate(X_train),
                           key=lambda (index, point): distance(test, point))
        yield y_train[index]


def oneNN(X_train, y_train, X_test):
    result = []
    for test in X_test:
        point,index = min([(distance(test,p),i) for i,p in enumerate(X_train)])
        result.append(y_train[index])
    return result

# -- expand to KNN
from collections import Counter


def KNN(X_train, y_train, X_test,k=1):
    result = []
    for test in X_test:
        s = sorted([(distance(test,p),i) for i,p in enumerate(X_train)])[:k]
        c = Counter([y_train[i] for j,i in s]).most_common()
        result.append(c[0][0])
    return result
